from rea.collections.contracts import ClauseDocumentCollection
from rea.market.models.patterns.subscription import SubscriptionClause
from rea.mongo import mongodb
from rea.collections.contracts import ContractDocumentCollection
from rea.market.models.patterns.subscription import SubscriptionContract



class SubscriptionClauseDocumentCollection(ClauseDocumentCollection):
    """
    A denormalized collection of `SubscriptionClause`
    """
    model = SubscriptionClause
    name = "market_subscription_clause"


class SubscriptionContractDocumentCollection(ContractDocumentCollection):
    """
    A denormalized collection of `SubscriptionContract`
    """
    model = SubscriptionContract
    name = "market_subscription_contract"


mongodb.register(SubscriptionClauseDocumentCollection())
mongodb.register(SubscriptionContractDocumentCollection())
