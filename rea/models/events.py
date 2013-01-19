import datetime

from django.db import models
from polymorphic.polymorphic_model import PolymorphicModel

from .reciprocity import *


class Event(PolymorphicModel):
    '''
    An Event _might_ be the result of an earlier Commitment event
    so we provide an optional fk relationship.
    '''
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

    # uuid = models.UUIDField() TODO get this from UUIDMixin

    agent = models.ForeignKey(
        'Agent')

    resource = models.ForeignKey(
        'Resource')

    quantity = models.PositiveIntegerField()

    class Meta:
        app_label = "rea"


class IncrementEvent(EventLineMixin, Increment):

    event = models.ForeignKey(
        'Event')

    class Meta:
        app_label = "rea"


class DecrementEvent(EventLineMixin, Decrement):

    event = models.ForeignKey(
        'Event')

    class Meta:
        app_label = "rea"
