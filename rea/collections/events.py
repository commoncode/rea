from rea.mongo import mongodb, DRFDocumentCollection
from rea.serializers.events import (
    EventSerializer, IncrementEventSerializer, DecrementEventSerializer
)


class EventDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Event`
    """
    name = "event"
    serializer_class = EventSerializer


class IncrementEventDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `IncrementEvent`
    """
    parent_collection = EventDocumentCollection
    name = "increment_event"
    serializer_class = IncrementEventSerializer


class DecrementEventDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `DecrementEvent`
    """
    parent_collection = EventDocumentCollection
    name = "decrement_event"
    serializer_class = DecrementEventSerializer


mongodb.register(EventDocumentCollection())
mongodb.register(IncrementEventDocumentCollection())
mongodb.register(DecrementEventDocumentCollection())
