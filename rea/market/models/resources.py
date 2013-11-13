import logging
from django.db import models

from rea.models.resources import Resource

logger = logging.getLogger(__name__)


class Currency(Resource):
    """
    Currency resource
    """
    class Meta:
        app_label = 'market'


class Product(Resource):
    """
    Product resource
    """
    price = models.FloatField()

    class Meta:
        app_label = 'market'


class Subscription(Product):
    """
    Subscription resource
    """
    class Meta:
        app_label = 'market'
