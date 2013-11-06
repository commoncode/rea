from rea.mongo import mongodb
from rea.collections.contracts import (
    ClauseDocumentCollection, ContractDocumentCollection
)
from rea.market.patterns.subscription.models import (
    SubscriptionContract, SubscriptionClause
)


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
