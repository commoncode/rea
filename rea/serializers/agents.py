from rea.models.agents import Agent
from rea.serializers.core import REASerializer


class AgentSerializer(REASerializer):
    """
    Serializer for the `SubscriptionContract` model
    """
    class Meta:
        model = Agent
        fields = (
            "id", "title", "short_title"
        )
