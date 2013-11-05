import logging

from rea.models.resources import Resource

logger = logging.getLogger(__name__)


class Currency(Resource):
    """
    Currency resource
    """
    class Meta:
        app_label = 'market'


class Subscription(Resource):
    """
    Subscription resource
    """
    class Meta:
        app_label = 'market'
