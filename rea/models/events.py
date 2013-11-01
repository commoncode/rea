from django.db import models
from polymorphic.polymorphic_model import PolymorphicModel
from django_xworkflows import models as xwf_models
from denormalize.models import DocumentCollection

from rea.models.reciprocity import Increment, Decrement
from rea.mongo import mongodb


###########################################################
#  Django Models                                          #
###########################################################


class Event(PolymorphicModel):
    """
    An Event _might_ be the result of an earlier Commitment event
    so we provide an optional fk relationship.
    """
    related_commitment = models.ForeignKey(
        'rea.Commitment',
        blank=True,
        null=True,
        related_name='%(app_label)s_%(class)s_commitment')

    occurance = models.DateTimeField(
        blank=True,
        null=True)

    occured_at = models.TextField()

    class Meta:
        app_label = "rea"


class EventLineMixin(PolymorphicModel):
    """
    """
    agent = models.ForeignKey(
        'Agent')

    resource = models.ForeignKey(
        'Resource')

    quantity = models.PositiveIntegerField()

    class Meta:
        app_label = "rea"
        abstract = True


class IncrementEvent(EventLineMixin, Increment):
    """
    """
    event = models.ForeignKey(
        'Event')

    class Meta:
        app_label = "rea"


class DecrementEvent(EventLineMixin, Decrement):
    """
    """
    event = models.ForeignKey(
        'Event')

    class Meta:
        app_label = "rea"


###########################################################
#  Denormalize Document Collections                       #
###########################################################


class EventDocumentCollection(DocumentCollection):
    """
    A denormalized collection of `Event`
    """
    model = Event
    name = "rea_event"
    # FIXME: Not working?
    # select_related = ['related_commitment']


class IncrementEventDocumentCollection(DocumentCollection):
    """
    A denormalized collection of `IncrementEvent`
    """
    model = IncrementEvent
    name = "rea_increment_event"
    select_related = ['event', 'agent', 'resource']


class DecrementEventDocumentCollection(DocumentCollection):
    """
    A denormalized collection of `DecrementEvent`
    """
    model = DecrementEvent
    name = "rea_decrement_event"
    select_related = ['event', 'agent', 'resource']


###########################################################
#  Mongodb registers                                      #
###########################################################


mongodb.register(EventDocumentCollection())
mongodb.register(IncrementEventDocumentCollection())
mongodb.register(DecrementEventDocumentCollection())
