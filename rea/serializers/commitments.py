from rea.models.commitments import (
    Commitment, IncrementCommitment, DecrementCommitment
)
from rea.serializers.core import REASerializer
from rea.serializers.resources import ResourceSerializer
from rea.serializers.agents import AgentSerializer
from rea.serializers.events import IncrementEventSerializer
from rea.serializers.events import DecrementEventSerializer
# from rea.serializers.contracts import ContractSerializer




class IncrementCommitmentSerializer(REASerializer):
    """
    Serializer for the `IncrementCommitment` model
    """
    resource = ResourceSerializer()
    agent = AgentSerializer()

    class Meta:
        model = IncrementCommitment
        fields = (
            "id", "agent", "resource", "quantity", "commitment"
        )


class DecrementCommitmentSerializer(REASerializer):
    """
    Serializer for the `DecrementCommitment` model
    """
    agent = AgentSerializer()
    resource = ResourceSerializer()

    class Meta:
        model = DecrementCommitment
        fields = (
            "id", "agent", "resource", "quantity", "commitment"
        )


class CommitmentSerializer(REASerializer):
    """
    Serializer for the `SubscriptionContract` model
    """
    increment_events = IncrementEventSerializer(
        source="incrementevent_set", many=True
    )

    decrement_events = DecrementEventSerializer(
        source="decrementevent_set", many=True
    )

    class Meta:
        model = Commitment
        fields = (
            "id", "related_commitment", "occured_at",
            "increment_events", "decrement_events"
        )
