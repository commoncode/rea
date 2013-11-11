from rea.models.events import Event, IncrementLine, DecrementLine
from rea.serializers.core import REASerializer
from rea.serializers.agents import AgentSerializer
from rea.serializers.resources import ResourceSerializer
from rea.serializers.contracts import ContractSerializer
from rea.serializers.commitments import CommitmentSerializer


class IncrementLineSerializer(REASerializer):
    """
    Serializer for the `IncrementLine` model
    """
    contract = ContractSerializer()
    providing_agent = AgentSerializer()
    recieving_agent = AgentSerializer()
    resource = ResourceSerializer()

    class Meta:
        model = IncrementLine
        fields = (
            "id", "providing_agent", "recieving_agent",
            "resource", "quantity"
        )


class DecrementLineSerializer(REASerializer):
    """
    Serializer for the `DecrementLine` model
    """
    contract = ContractSerializer()
    providing_agent = AgentSerializer()
    recieving_agent = AgentSerializer()
    resource = ResourceSerializer()

    class Meta:
        model = DecrementLine
        fields = (
            "id", "providing_agent", "recieving_agent",
            "resource", "quantity"
        )


class EventSerializer(REASerializer):
    """
    Serializer for the `Event` model
    """
    commitment = CommitmentSerializer()
    increment = IncrementLineSerializer()
    decrement = DecrementLineSerializer()

    class Meta:
        model = Event
        fields = (
            "id", "commitment", "occured_at",
            "increment", "decrement"
        )

