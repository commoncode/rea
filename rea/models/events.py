from django.db import models

from rea.models.reciprocity import Increment, Decrement
from rea.models.core import REAModel


class Event(REAModel):
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


class EventLineMixin(REAModel):
    """
    """
    agent = models.ForeignKey('Agent')
    resource = models.ForeignKey('Resource')
    quantity = models.PositiveIntegerField()

    class Meta:
        app_label = "rea"
        abstract = True


class IncrementEvent(EventLineMixin, Increment):
    """
    """
    event = models.ForeignKey(Event)

    class Meta:
        app_label = "rea"


class DecrementEvent(EventLineMixin, Decrement):
    """
    """
    event = models.ForeignKey(Event)

    class Meta:
        app_label = "rea"
