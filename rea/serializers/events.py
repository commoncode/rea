from rea.models.events import Event, IncrementEvent, DecrementEvent
from rea.serializers.core import REASerializer
from rea.serializers.commitments import CommitmentSerializer
from rea.serializers.agents import AgentSerializer


class EventSerializer(REASerializer):
    """
    Serializer for the `Event` model
    """
    related_commitment = CommitmentSerializer()

    class Meta:
        model = Event
        fields = (
            "id", "related_commitment", "occurance", "occured_at"
        )


class IncrementEventSerializer(REASerializer):
    """
    Serializer for the `IncrementEvent` model
    """
    agent = AgentSerializer()
    # resource = ResourceSerializer()
    event = EventSerializer()

    class Meta:
        model = IncrementEvent
        fields = (
            "id", "agent", "resource", "quantity", "event"
        )


class DecrementEventSerializer(REASerializer):
    """
    Serializer for the `DecrementEvent` model
    """
    agent = AgentSerializer()
    # resource = ResourceSerializer()
    event = EventSerializer()

    class Meta:
        model = DecrementEvent
        fields = (
            "id", "agent", "resource", "quantity", "event"
        )
