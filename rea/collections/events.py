from rea.mongo import mongodb, DRFDocumentCollection
from rea.serializers.events import (
    EventSerializer, IncrementEventSerializer, DecrementEventSerializer,
    ExchangeEventSerializer
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


class ExchangeEventDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `ExchangeEvent`
    """
    name = "exchange_event"
    serializer_class = ExchangeEventSerializer


mongodb.register(EventDocumentCollection())
mongodb.register(IncrementEventDocumentCollection())
mongodb.register(DecrementEventDocumentCollection())
mongodb.register(ExchangeEventDocumentCollection())

