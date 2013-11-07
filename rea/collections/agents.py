from rea.mongo import mongodb, DRFDocumentCollection
from rea.serializers.agents import AgentSerializer


class AgentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Agent`
    """
    serializer_class = AgentSerializer
    name = "agent"


mongodb.register(AgentDocumentCollection())
