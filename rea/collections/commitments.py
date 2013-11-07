from rea.mongo import mongodb, DRFDocumentCollection
from rea.serializers.commitments import (
    CommitmentSerializer, IncrementCommitmentSerializer,
    DecrementCommitmentSerializer
)
from rea.collections.reciprocity import (
    IncrementDocumentCollection, DecrementDocumentCollection
)
from rea.collections.events import EventDocumentCollection


class CommitmentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Commitment`
    """
    parent_collection = EventDocumentCollection
    name = "commitment"
    serializer_class = CommitmentSerializer


class IncrementCommitmentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `IncrementCommitment`
    """
    parent_collection = IncrementDocumentCollection
    name = "increment_commitment"
    serializer_class = IncrementCommitmentSerializer


class DecrementCommitmentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `DecrementCommitment`
    """
    parent_collection = DecrementDocumentCollection
    name = "decrement_commitment"
    serializer_class = DecrementCommitmentSerializer


mongodb.register(CommitmentDocumentCollection())
mongodb.register(IncrementCommitmentDocumentCollection())
mongodb.register(DecrementCommitmentDocumentCollection())
