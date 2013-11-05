from rea.mongo import mongodb, DRFDocumentCollection
from rea.market.serializers.agents import (
    CustomerSerializer, EnterpriseSerializer
)


class CustomerDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Customer`
    """
    serializer_class = CustomerSerializer
    name = "market_customer"


class EnterpriseDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Enterprise`
    """
    serializer_class = EnterpriseSerializer
    name = "market_enterprise"


mongodb.register(CustomerDocumentCollection())
mongodb.register(EnterpriseDocumentCollection())
import ipdb; ipdb.set_trace();
