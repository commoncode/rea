from rea.mongo import mongodb, DRFDocumentCollection
from rea.models.agents import Agent


class AgentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Agent`
    """
    serializer_class = "rea.serializers.agents.AgentSerializer"
    model = Agent
    name = "agent"


mongodb.register(AgentDocumentCollection())
