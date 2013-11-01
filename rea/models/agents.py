from polymorphic.polymorphic_model import PolymorphicModel
from entropy.base import SlugMixin, TitleMixin
from denormalize.models import DocumentCollection
from rest_framework import serializers
from rea.mongo import mongodb, DRFDocumentCollection


###########################################################
#  Django Models                                          #
###########################################################


class Agent(PolymorphicModel, TitleMixin, SlugMixin):

    class Meta:
        app_label = "rea"


###########################################################
#  Model Serializers                                      #
###########################################################


class AgentSerializer(serializers.ModelSerializer):
    """
    Serializer for the `SubscriptionContract` model
    """
    class Meta:
        model = Agent
        fields = (
            "id", "title", "short_title", "slug"
        )


###########################################################
#  Denormalize Document Collections                       #
###########################################################


class AgentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Agent`
    """
    serializer_class = AgentSerializer
    name = "rea_agent"


###########################################################
#  Mongodb registers                                      #
###########################################################


mongodb.register(AgentDocumentCollection())
