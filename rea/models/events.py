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

    occured_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True
        )

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


class IncrementEvent(EventLineMixin):
    """
    """
    event = models.ForeignKey(Event)

    class Meta:
        app_label = "rea"


class DecrementEvent(EventLineMixin):
    """
    """
    event = models.ForeignKey(Event)

    class Meta:
        app_label = "rea"


class ExchangeEvent(REAModel):
    """
    An Event exchange (A convenient model to dictate both sides of an exchange)
    """
    increment = models.ForeignKey(IncrementEvent)
    decrement = models.ForeignKey(DecrementEvent)

    class Meta:
        app_label = "rea"

