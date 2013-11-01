from rea.models.agents import Agent, AgentDocumentCollection
from rea.mongo import mongodb


###########################################################
#  Django Models                                          #
###########################################################


class Customer(Agent):
    """
    A customer agent (buyer)
    """
    class Meta:
        app_label = 'market'


class Enterprise(Agent):
    """
    An enterprise agent (seller)
    """
    class Meta:
        app_label = 'market'


###########################################################
#  Denormalize Document Collections                       #
###########################################################


class CustomerDocumentCollection(AgentDocumentCollection):
    """
    A denormalized collection of `Customer`
    """
    model = Customer
    name = "market_customer"


class EnterpriseDocumentCollection(AgentDocumentCollection):
    """
    A denormalized collection of `Enterprise`
    """
    model = Enterprise
    name = "market_enterprise"


###########################################################
#  Mongodb registers                                      #
###########################################################


mongodb.register(CustomerDocumentCollection())
mongodb.register(EnterpriseDocumentCollection())
