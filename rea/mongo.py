import logging
from django.conf import settings
from denormalize.backend.mongodb import MongoBackend
from denormalize.models import DocumentCollection

logger = logging.getLogger(__name__)


REA_MONGO_DB_NAME = getattr(settings,
    "REA_MONGO_DB_NAME", "rea_denormalized")
REA_MONGO_CONNECTION_URI = getattr(settings,
    "REA_MONGO_DB_NAME", "mongodb://localhost")


mongodb = MongoBackend(
    name='mongo',
    db_name=REA_MONGO_DB_NAME,
    connection_uri=REA_MONGO_CONNECTION_URI
)


class DRFDocumentCollection(DocumentCollection):
    """
    Overrides `DocumentCollection` to make use of the Django Rest Framework
    serializer for serializing our objects. This provides more power in
    what data we want to retrieve.
    """
    serializer_class = None

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
        data = self.serializer_class(obj).data
        logger.debug(data)
        return data
