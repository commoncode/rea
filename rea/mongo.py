import logging
import pymongo
import importlib

from django.conf import settings
from denormalize.backend.mongodb import MongoBackend
from denormalize.models import DocumentCollection


logger = logging.getLogger(__name__)


REA_MONGO_DB_NAME = getattr(settings,
    "REA_MONGO_DB_NAME", "rea_denormalized")
REA_MONGO_CONNECTION_URI = getattr(settings,
    "REA_MONGO_URI", "mongodb://localhost")


class REAMongoBackend(MongoBackend):
    db_name = "test_denormalize"

    def get_mongo_id(self, collection, doc_id):
        return collection.model.objects.get(id=doc_id).mongoID

    def connect(self):
        self.connection = pymongo.Connection(self.connection_uri, safe=True)
        self.db = getattr(self.connection, self.db_name)

    def get_parent_table_name(self, collection, table_name):
        return "%s__%s" % (
            collection.parent_collection.name,
            table_name
        )

    def deleted(self, collection, doc_id):
        mongoID = self.get_mongo_id(collection, doc_id)
        while True:
            has_parent = False
            table_name = collection.name
            if collection.parent_collection:
                table_name = self.get_parent_table_name(
                    collection, table_name
                )
                has_parent = True

            logging.debug('deleted: %s %s', collection.name, doc_id)
            col = getattr(self.db, collection.name)
            col.remove({'_id': mongoID})

            if not has_parent:
                break
            collection = collection.parent_collection

    def added(self, collection, doc_id, doc):
        # We can share the same ID across
        mongoID = self.get_mongo_id(collection, doc_id)
        is_parent = True
        parent_table_name = collection.name
        while True:
            has_parent = False
            table_name = collection.name
            if collection.parent_collection:
                table_name = self.get_parent_table_name(
                    collection, table_name
                )
                has_parent = True

            logging.debug('added: %s %s', table_name, doc_id)
            col = getattr(self.db, table_name)
            # Replace any existing document
            doc['_id'] = mongoID
            if not is_parent:
                doc['_parent_table'] = parent_table_name
            col.update({'_id': mongoID}, doc, upsert=True)

            if not has_parent:
                break
            collection = collection.parent_collection
            is_parent = False

    def changed(self, collection, doc_id, doc):
        mongoID = self.get_mongo_id(collection, doc_id)

        while True:
            has_parent = False
            table_name = collection.name
            if collection.parent_collection:
                table_name = self.get_parent_table_name(
                    collection, table_name
                )
                has_parent = True

            logging.debug('changed: %s %s', collection.name, doc_id)
            col = getattr(self.db, table_name)
            # We are not allowed to update _id
            if '_id' in doc:
                del doc['_id']
            # Only update the documents fields. We keep any other fields
            # added by other code intact, as long as they are set on the
            # document root.
            col.update({'_id': mongoID}, {'$set': doc}, upsert=True)

            if not has_parent:
                break
            collection = collection.parent_collection

    def get_doc(self, collection, doc_id):
        mongoID = self.get_mongo_id(collection, doc_id)
        col = getattr(self.db, collection.name)
        return col.find_one({'_id': mongoID})


mongodb = REAMongoBackend(
    name='mongo',
    db_name=REA_MONGO_DB_NAME,
    connection_uri=REA_MONGO_CONNECTION_URI
)


class DRFDocumentCollection(DocumentCollection):
    """
    Overrides `DocumentCollection` to make use of the Django Rest Framework
    serializer for serializing our objects. This provides more power in
    what data we want to retrieve.

    TODO: How to deal with stale foreign key data being cached in mongo?
    """
    serializer_class = None

    # Parent DRFDocumentCollection (for saving child objects)
    parent_collection = None

    def __init__(self):
        if self.serializer_class is None:
            raise ValueError("serializer_class can not be None")
        if self.model is None:
            self.model = self.serializer_class.Meta.model
        if not self.name:
            self.name = self.model._meta.db_table

    def get_related_models(self):
        """
        Override the get_related_models to disable the function. This will
        be done with Django Rest Framework instead
        """
        return {}

    def dump_obj(self, model, obj, path):
        """
        Use Django Rest Framework to serialize our object
        """
        if isinstance(self.serializer_class, str):
            # If a string, import and get the class
            mods = self.serializer_class.split('.')
            class_str = mods[-1]
            path_str = '.'.join(mods[:-1])
            module = importlib.import_module(path_str)
            self.serializer_class = getattr(module, class_str)

        data = self.serializer_class(obj).data
        logger.debug('\033[94m%s:\033[0m %s' % (model._meta.db_table, data))
        return data
