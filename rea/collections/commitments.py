from rea.mongo import mongodb, DRFDocumentCollection
from rea.serializers.commitments import (
    CommitmentSerializer, IncrementCommitmentSerializer,
    DecrementCommitmentSerializer
)


class CommitmentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Commitment`
    """
    name = "commitment"
    serializer_class = CommitmentSerializer


class IncrementCommitmentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `IncrementCommitment`
    """
    name = "increment_commitment"
    serializer_class = IncrementCommitmentSerializer


class DecrementCommitmentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `DecrementCommitment`
    """
    name = "decrement_commitment"
    serializer_class = DecrementCommitmentSerializer


mongodb.register(CommitmentDocumentCollection())
mongodb.register(IncrementCommitmentDocumentCollection())
mongodb.register(DecrementCommitmentDocumentCollection())
