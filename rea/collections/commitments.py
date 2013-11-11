from rea.mongo import mongodb, DRFDocumentCollection
from rea.collections.events import EventDocumentCollection
from rea.models.commitments import (
    Commitment, IncrementCommitment, DecrementCommitment
)

class CommitmentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Commitment`
    """
    name = "commitment"
    model = Commitment
    serializer_class = "rea.serializers.commitments.CommitmentSerializer"


class IncrementCommitmentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `IncrementCommitment`
    """
    name = "increment_commitment"
    model = IncrementCommitment
    serializer_class = (
        "rea.serializers.commitments.IncrementCommitmentSerializer")


class DecrementCommitmentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `DecrementCommitment`
    """
    name = "decrement_commitment"
    model = DecrementCommitment
    serializer_class = (
        "rea.serializers.commitments.DecrementCommitmentSerializer")


mongodb.register(CommitmentDocumentCollection())
mongodb.register(IncrementCommitmentDocumentCollection())
mongodb.register(DecrementCommitmentDocumentCollection())
