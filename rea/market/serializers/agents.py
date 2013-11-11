from rea.serializers.agents import AgentSerializer
from rea.market.models.agents import Customer, Enterprise


class CustomerSerializer(AgentSerializer):
    """
    Serializer for the `SubscriptionContract` model
    """
    class Meta(AgentSerializer.Meta):
        model = Customer
        fields = AgentSerializer.Meta.fields + (
            'date_joined',
        )


class EnterpriseSerializer(AgentSerializer):
    """
    Serializer for the `SubscriptionContract` model
    """
    class Meta(AgentSerializer.Meta):
        model = Enterprise
