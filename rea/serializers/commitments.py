from rea.models.commitments import (
    Commitment, IncrementCommitment, DecrementCommitment
)
from rea.serializers.core import REASerializer
from rea.serializers.resources import ResourceSerializer
from rea.serializers.agents import AgentSerializer
# from rea.serializers.contracts import ContractSerializer


class CommitmentSerializer(REASerializer):
    """
    Serializer for the `SubscriptionContract` model
    """
    # contract = ContractSerializer()

    class Meta:
        model = Commitment
        fields = (
            "id", "related_commitment", "occured_at"
        )

class IncrementCommitmentSerializer(REASerializer):
    """
    Serializer for the `IncrementCommitment` model
    """
    commitment = CommitmentSerializer()
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
    commitment = CommitmentSerializer()
    agent = AgentSerializer()
    resource = ResourceSerializer()

    class Meta:
        model = DecrementCommitment
        fields = (
            "id", "agent", "resource", "quantity", "commitment"
        )
