from django.db import models

from cqrs.models import CQRSPolymorphicModel

from . import LineMixin


class CommitmentLineMixin(LineMixin):

    class Meta:
        abstract = True


class IncrementCommitment(CommitmentLineMixin):
    pass


class DecrementCommitment(CommitmentLineMixin):
    pass


class Commitment(CQRSPolymorphicModel):
    '''
    Essentially our reciprocity
    '''
    contract = models.ForeignKey('rea.Contract')

    occured_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True
    )

    increment = models.ForeignKey(
        IncrementCommitment,
        related_name='%(app_label)s_%(class)s_increment_commitments'
    )
    decrement = models.ForeignKey(
        DecrementCommitment,
        related_name='%(app_label)s_%(class)s_decrement_commitments'
    )