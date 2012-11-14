from django.db import models
from polymorphic.polymorphic_model import PolymorphicModel

from .reciprocity import *

class Event(PolymorphicModel):

    # uuid = models.UUIDField() TODO get this from UUIDMixin

    agent = models.ForeignKey(
        'Agent')

    resource = models.ForeignKey(
        'Resource')

    quantity = models.PositiveIntegerField()

    occurance = models.DateTimeField()
    occured_at = models.TextField()

    class Meta:
        app_label = "rea"


class IncrementEvent(Event, Increment):

    class Meta:
        app_label = "rea"


class DecrementEvent(Event, Decrement):

    class Meta:
        app_label = "rea"
