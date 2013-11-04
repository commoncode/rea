from django.db import models
from rea.models.core import REAModel


class Increment(REAModel):
    pass

    class Meta:
        app_label = "rea"


class Decrement(REAModel):
    pass

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
