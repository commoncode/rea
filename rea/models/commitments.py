from django.db import models
from polymorphic.polymorphic_model import PolymorphicModel

from .reciprocity import *


class Commitment(PolymorphicModel):

    contract = models.ForeignKey(
        'rea.Contract')

    class Meta:
        app_label = "rea"


class CommitmentLine(PolymorphicModel):

    commitment = models.ForeignKey(
        'Commitment')

    agent = models.ForeignKey(
        'rea.Agent')

    resource = models.ForeignKey(
        'rea.Resource')

    quantity = models.PositiveIntegerField()

    class Meta:
        app_label = "rea"


class IncrementCommitment(CommitmentLine, Increment):

    class Meta:
        app_label = "rea"


class DecrementCommitment(CommitmentLine, Decrement):

    class Meta:
        app_label = "rea"