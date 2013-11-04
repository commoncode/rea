from rea.models.commitments import (
    Commitment, IncrementCommitment, DecrementCommitment
)
from rea.serializers.core import REASerializer


class CommitmentSerializer(REASerializer):
    """
    Serializer for the `SubscriptionContract` model
    """
    # contract = ContractSerializer()

    class Meta:
        model = Commitment
        fields = (
            "id", "related_commitment", "occurance", "occured_at",
            "contract"
        )


class IncrementCommitmentSerializer(REASerializer):
    """
    Serializer for the `IncrementCommitment` model
    """
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

    class Meta:
        model = DecrementCommitment
        fields = (
            "id", "agent", "resource", "quantity", "commitment"
        )
