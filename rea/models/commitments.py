from django.db import models
from polymorphic.polymorphic_model import PolymorphicModel

from .events import *
from .reciprocity import *


class Commitment(Event):

    contract = models.ForeignKey(
        'rea.Contract')

    class Meta:
        app_label = "rea"

    def is_fulfilled(self):
        '''Query the Ledger or Event table for an Event with Event.commitment == self
        from this we infer that the commitment event has been fulfilled by a
        transactional event'''
        try:
            event = Event.objects.get(commitment=self)
        except Event.DoesNotExist:
            return False
        return True

class CommitmentLineMixin(EventLineMixin):

    commitment = models.ForeignKey(
        'Commitment')

    class Meta:
        abstract = True


class IncrementCommitment(CommitmentLineMixin, Increment):

    class Meta:
        app_label = "rea"


class DecrementCommitment(CommitmentLineMixin, Decrement):

    class Meta:
        app_label = "rea"