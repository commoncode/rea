from django.db import models
from polymorphic.polymorphic_model import PolymorphicModel
from denormalize.models import DocumentCollection
from rea.mongo import mongodb



###########################################################
#  Django Models                                          #
###########################################################


class Increment(PolymorphicModel):
    pass

    class Meta:
        app_label = "rea"


class Decrement(PolymorphicModel):
    pass

    class Meta:
        app_label = "rea"


class Reciprocity(PolymorphicModel):
    """
    Through model that links:

        * Incrementing/Decrementing Events & Commitments
    """
    increment = models.ForeignKey(Increment)
    decrement = models.ForeignKey(Decrement)

    class Meta:
        app_label = "rea"


###########################################################
#  Denormalize Document Collections                       #
###########################################################


class IncrementDocumentCollection(DocumentCollection):
    """
    A denormalized collection of `Increment`
    """
    model = Increment
    name = "rea_increment"


class DecrementDocumentCollection(DocumentCollection):
    """
    A denormalized collection of `Decrement`
    """
    model = Decrement
    name = "rea_decrement"


class ReciprocityDocumentCollection(DocumentCollection):
    """
    A denormalized collection of `Reciprocity`
    """
    model = Reciprocity
    name = "rea_reciprocity"
    select_related = ['increment', 'decrement']


###########################################################
#  Mongodb registers                                      #
###########################################################


mongodb.register(IncrementDocumentCollection())
mongodb.register(DecrementDocumentCollection())
mongodb.register(ReciprocityDocumentCollection())


