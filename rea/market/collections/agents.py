from rea.mongo import mongodb, DRFDocumentCollection
from rea.collections.agents import AgentDocumentCollection
from core.models import Customer
from rea.market.models.agents import Enterprise


class CustomerDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Customer`
    """
    parent_collection = AgentDocumentCollection
    model = Customer
    serializer_class = "rea.market.serializers.agents.CustomerSerializer"
    name = "market_customer"


class EnterpriseDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Enterprise`
    """
    parent_collection = AgentDocumentCollection
    model = Enterprise
    serializer_class = "rea.market.serializers.agents.EnterpriseSerializer"
    name = "market_enterprise"


mongodb.register(CustomerDocumentCollection())
mongodb.register(EnterpriseDocumentCollection())
