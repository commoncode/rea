from rea.serializers.resources import ResourceSerializer
from rea.market.models.resources import Currency, Subscription, Product


class CurrencySerializer(ResourceSerializer):
    """
    Serializer for the `Currency` model
    """
    class Meta(ResourceSerializer.Meta):
        model = Currency


class ProductSerializer(ResourceSerializer):
    """
    Serializer for the `Product` model
    """
    class Meta(ResourceSerializer.Meta):
        model = Product
        fields = ResourceSerializer.Meta.fields + (
            'price',
        )


class SubscriptionSerializer(ProductSerializer):
    """
    Serializer for the `Subscription` model
    """
    class Meta(ProductSerializer.Meta):
        model = Subscription
