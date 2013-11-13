from rea.mongo import mongodb, DRFDocumentCollection
from rea.collections.resources import ResourceDocumentCollection
from rea.market.models.resources import Currency, Subscription, Product


class CurrencyDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Currency`
    """
    parent_collection = ResourceDocumentCollection
    model = Currency
    serializer_class = "rea.market.serializers.resources.CurrencySerializer"
    name = "currency"


class ProductDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Subscription`
    """
    parent_collection = ResourceDocumentCollection
    model = Product
    serializer_class = "rea.market.serializers.resources.ProductSerializer"
    name = "product"


class SubscriptionDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Subscription`
    """
    parent_collection = ResourceDocumentCollection
    model = Subscription
    serializer_class = "rea.market.serializers.resources.SubscriptionSerializer"
    name = "subscription"


mongodb.register(CurrencyDocumentCollection())
mongodb.register(ProductDocumentCollection())
mongodb.register(SubscriptionDocumentCollection())
