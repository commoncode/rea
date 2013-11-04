from rea.models.agents import Agent
from rea.serializers.agents import AgentSerializer
from rea.mongo import mongodb, DRFDocumentCollection


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
#  Model Serializers                                      #
###########################################################


class CustomerSerializer(AgentSerializer):
    """
    Serializer for the `SubscriptionContract` model
    """
    class Meta(AgentSerializer.Meta):
        model = Customer


class EnterpriseSerializer(AgentSerializer):
    """
    Serializer for the `SubscriptionContract` model
    """
    class Meta(AgentSerializer.Meta):
        model = Enterprise


###########################################################
#  Denormalize Document Collections                       #
###########################################################


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


###########################################################
#  Mongodb registers                                      #
###########################################################


mongodb.register(CustomerDocumentCollection())
mongodb.register(EnterpriseDocumentCollection())
