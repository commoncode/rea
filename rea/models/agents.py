from polymorphic.polymorphic_model import PolymorphicModel
from entropy.base import SlugMixin, TitleMixin
from denormalize.models import DocumentCollection
from rea.mongo import mongodb


###########################################################
#  Django Models                                          #
###########################################################


class Agent(PolymorphicModel, TitleMixin, SlugMixin):

    class Meta:
        app_label = "rea"


###########################################################
#  Denormalize Document Collections                       #
###########################################################


class AgentDocumentCollection(DocumentCollection):
    """
    A denormalized collection of `Agent`
    """
    model = Agent
    name = "rea_agent"


###########################################################
#  Mongodb registers                                      #
###########################################################


mongodb.register(AgentDocumentCollection())
