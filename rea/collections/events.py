from rea.mongo import mongodb, DRFDocumentCollection
from rea.models.events import Event, DecrementLine, IncrementLine


class EventDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Event`
    """
    name = "event"
    model = Event
    serializer_class = "rea.serializers.events.EventSerializer"


class IncrementLineDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `IncrementLine`
    """
    name = "increment_line"
    model = IncrementLine
    serializer_class = "rea.serializers.events.IncrementLineSerializer"


class DecrementLineDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `DecrementLine`
    """
    name = "decrement_line"
    model = DecrementLine
    serializer_class = "rea.serializers.events.DecrementLineSerializer"


mongodb.register(EventDocumentCollection())
mongodb.register(IncrementLineDocumentCollection())
mongodb.register(DecrementLineDocumentCollection())

