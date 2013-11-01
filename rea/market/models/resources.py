import logging
from rea.models.resources import Resource, ResourceDocumentCollection
from rea.mongo import mongodb

logger = logging.getLogger(__name__)


###########################################################
#  Django Models                                          #
###########################################################


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


###########################################################
#  Denormalize Document Collections                       #
###########################################################


class CurrencyDocumentCollection(ResourceDocumentCollection):
    """
    A denormalized collection of `Currency`
    """
    model = Currency
    name = "market_currency"


class SubscriptionDocumentCollection(ResourceDocumentCollection):
    """
    A denormalized collection of `Subscription`
    """
    model = Subscription
    name = "market_subscription"


###########################################################
#  Mongodb registers                                      #
###########################################################


mongodb.register(CurrencyDocumentCollection())
mongodb.register(SubscriptionDocumentCollection())

