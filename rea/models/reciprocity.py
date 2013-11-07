from django.db import models
from rea.models.core import REAModel


class Increment(REAModel):

    class Meta:
        app_label = "rea"


class Decrement(REAModel):

    class Meta:
        app_label = "rea"


class Reciprocity(REAModel):
    """
    Through model that links:

        * Incrementing/Decrementing Events & Commitments
    """
    increment = models.ForeignKey(Increment)
    decrement = models.ForeignKey(Decrement)

    class Meta:
        app_label = "rea"
