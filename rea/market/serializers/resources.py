from rea.serializers.resources import ResourceSerializer
from rea.market.models.resources import Currency, Subscription


class CurrencySerializer(ResourceSerializer):
    """
    Serializer for the `Currency` model
    """
    class Meta(ResourceSerializer.Meta):
        model = Currency


class SubscriptionSerializer(ResourceSerializer):
    """
    Serializer for the `Subscription` model
    """
    class Meta(ResourceSerializer.Meta):
        model = Subscription
