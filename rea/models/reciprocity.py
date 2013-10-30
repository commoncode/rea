from django.db import models
from polymorphic.polymorphic_model import PolymorphicModel


class Reciprocity(PolymorphicModel):
    """
    Through model that links:

        * Incrementing/Decrementing Events & Commitments
    """

    increment = models.ForeignKey(
        'Increment')

    decrement = models.ForeignKey(
        'Decrement')

    class Meta:
        app_label = 'rea'


class Increment(PolymorphicModel):

    class Meta:
        app_label = 'rea'


class Decrement(PolymorphicModel):

    class Meta:
        app_label = 'rea'
