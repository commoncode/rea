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
            "id", "related_commitment", "occurance", "occured_at"
        )

    def __init__(self, *args, **kwargs):
        super(CommitmentSerializer, self).__init__(*args, **kwargs)


class IncrementCommitmentSerializer(REASerializer):
    """
    Serializer for the `IncrementCommitment` model
    """
    commitment = CommitmentSerializer()
    resource = ResourceSerializer()
    agent = AgentSerializer()
    commitment = CommitmentSerializer()

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
    commitment = CommitmentSerializer()

    class Meta:
        model = DecrementCommitment
        fields = (
            "id", "agent", "resource", "quantity", "commitment"
        )
