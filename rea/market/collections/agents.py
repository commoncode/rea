from rea.mongo import mongodb, DRFDocumentCollection
from rea.market.serializers.agents import (
    CustomerSerializer, EnterpriseSerializer
)
from rea.collections.agents import AgentDocumentCollection


class CustomerDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Customer`
    """
    parent_collection = AgentDocumentCollection
    serializer_class = CustomerSerializer
    name = "market_customer"


class EnterpriseDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Enterprise`
    """
    parent_collection = AgentDocumentCollection
    serializer_class = EnterpriseSerializer
    name = "market_enterprise"


mongodb.register(CustomerDocumentCollection())
mongodb.register(EnterpriseDocumentCollection())
