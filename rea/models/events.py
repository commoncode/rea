from django.db import models

from cqrs.mongo import CQRSPolymorphicModel
from rea.models import LineMixin


class IncrementLine(LineMixin):
    '''
    The increment flow exchange of an economic event
    (Ie, the increased cash)
    '''
    pass


class DecrementLine(LineMixin):
    '''
    The decrement flow exchange of an economic event
    (Ie, the decreased resource)
    '''
    pass


class Event(CQRSPolymorphicModel):
    '''
    Essentialy our ledger
    '''
    commitment = models.ForeignKey(
        'rea.Commitment',
        blank=True,
        null=True,
        related_name='%(app_label)s_%(class)s_commitment')

    occured_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True
    )

    increment = models.ForeignKey(IncrementLine)
    decrement = models.ForeignKey(DecrementLine)
