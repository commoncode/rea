from rea.mongo import mongodb, DRFDocumentCollection
from rea.serializers.reciprocity import (
    IncrementSerializer, DecrementSerializer, ReciprocitySerializer
)


class IncrementDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Increment`
    """
    serializer_class = IncrementSerializer
    name = "rea_increment"


class DecrementDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Decrement`
    """
    serializer_class = DecrementSerializer
    name = "rea_decrement"


class ReciprocityDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Reciprocity`
    """
    serializer_class = ReciprocitySerializer
    name = "rea_reciprocity"


mongodb.register(IncrementDocumentCollection())
mongodb.register(DecrementDocumentCollection())
mongodb.register(ReciprocityDocumentCollection())


