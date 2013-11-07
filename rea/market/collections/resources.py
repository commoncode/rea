from rea.market.serializers.resources import CurrencySerializer
from rea.mongo import mongodb, DRFDocumentCollection
from rea.collections.resources import ResourceDocumentCollection
from rea.market.serializers.resources import SubscriptionSerializer


class CurrencyDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Currency`
    """
    parent_collection = ResourceDocumentCollection
    serializer_class = CurrencySerializer
    name = "currency"


class SubscriptionDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Subscription`
    """
    parent_collection = ResourceDocumentCollection
    serializer_class = SubscriptionSerializer
    name = "subscription"


mongodb.register(CurrencyDocumentCollection())
mongodb.register(SubscriptionDocumentCollection())
