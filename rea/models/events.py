from django.db import models

from rea.models.reciprocity import Increment, Decrement
from rea.models.core import REAModel
from rea.models import LineMixin


class IncrementLine(LineMixin):
    """
    The increment flow exchange of an economic event
    (Ie, the increased cash)
    """

    class Meta:
        app_label = "rea"


class DecrementLine(LineMixin):
    """
    The decrement flow exchange of an economic event
    (Ie, the decreased resource)
    """

    class Meta:
        app_label = "rea"


class Event(REAModel):
    """
    Essentialy our ledger
    """
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

    class Meta:
        app_label = "rea"
