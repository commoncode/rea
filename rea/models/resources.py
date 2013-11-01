from django.db import models
from polymorphic.polymorphic_model import PolymorphicModel
from entropy.base import SlugMixin, TitleMixin
from denormalize.models import DocumentCollection
from rea.mongo import mongodb


###########################################################
#  Django Models                                          #
###########################################################


class Resource(PolymorphicModel, TitleMixin, SlugMixin):

    class Meta:
        app_label = "rea"


###########################################################
#  Denormalize Document Collections                       #
###########################################################


class ResourceDocumentCollection(DocumentCollection):
    """
    A denormalized collection of `Resource`
    """
    model = Resource
    name = "rea_resource"


###########################################################
#  Mongodb registers                                      #
###########################################################


mongodb.register(ResourceDocumentCollection())
