from django.conf import settings
from denormalize.backend.mongodb import MongoBackend


REA_MONGO_DB_NAME = getattr(settings,
    "REA_MONGO_DB_NAME", "rea_denormalized")
REA_MONGO_CONNTION_URI = getattr(settings,
    "REA_MONGO_DB_NAME", "mongodb://localhost")


mongodb = MongoBackend(
    name='mongo',
    db_name=REA_MONGO_DB_NAME,
    connection_uri=REA_MONGO_CONNTION_URI
)
