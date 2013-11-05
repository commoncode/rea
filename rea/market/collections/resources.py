from rea.market.serializers.resources import CurrencySerializer
from rea.mongo import mongodb
from rea.collections.resources import ResourceDocumentCollection
from rea.market.serializers.resources import SubscriptionSerializer


class CurrencyDocumentCollection(ResourceDocumentCollection):
    """
    A denormalized collection of `Currency`
    """
    serializer_class = CurrencySerializer
    name = "market_currency"


class SubscriptionDocumentCollection(ResourceDocumentCollection):
    """
    A denormalized collection of `Subscription`
    """
    serializer_class = SubscriptionSerializer
    name = "market_currency"


mongodb.register(CurrencyDocumentCollection())
mongodb.register(SubscriptionDocumentCollection())
