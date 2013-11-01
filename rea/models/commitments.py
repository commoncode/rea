from django.db import models
from rea.models.events import Event, EventLineMixin
from rea.models.reciprocity import Increment, Decrement
from denormalize.models import DocumentCollection
from rea.mongo import mongodb


###########################################################
#  Django Models                                          #
###########################################################


class Commitment(Event):
    """
    """
    contract = models.ForeignKey('rea.Contract')

    class Meta:
        app_label = "rea"

    def is_fulfilled(self):
        """
        Query the Ledger or Event table for an Event with Event.commitment == self
        from this we infer that the commitment event has been fulfilled by a
        transactional event
        """
        try:
            Event.objects.get(commitment=self)
        except Event.DoesNotExist:
            return False
        return True


class CommitmentLineMixin(EventLineMixin):
    """
    """
    commitment = models.ForeignKey('Commitment')

    class Meta:
        abstract = True


class IncrementCommitment(CommitmentLineMixin, Increment):
    """
    """
    class Meta:
        app_label = "rea"


class DecrementCommitment(CommitmentLineMixin, Decrement):
    """
    """
    class Meta:
        app_label = "rea"


###########################################################
#  Denormalize Document Collections                       #
###########################################################


class CommitmentDocumentCollection(DocumentCollection):
    """
    A denormalized collection of `Commitment`
    """
    model = Commitment
    name = "rea_commitment"
    select_related = ['contract', 'related_commitment']
    exclude_all = ['state']


class IncrementCommitmentDocumentCollection(DocumentCollection):
    """
    A denormalized collection of `IncrementCommitment`
    """
    model = IncrementCommitment
    name = "rea_increment_commitment"
    select_related = ['commitment']


class DecrementCommitmentDocumentCollection(DocumentCollection):
    """
    A denormalized collection of `DecrementCommitment`
    """
    model = DecrementCommitment
    name = "rea_decrement_commitment"
    select_related = ['commitment']


###########################################################
#  Mongodb registers                                      #
###########################################################


mongodb.register(CommitmentDocumentCollection())
mongodb.register(IncrementCommitmentDocumentCollection())
mongodb.register(DecrementCommitmentDocumentCollection())
