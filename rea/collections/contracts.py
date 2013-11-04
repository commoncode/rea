from rea.mongo import mongodb, DRFDocumentCollection
from rea.serializers.contracts import (
    ContractSerializer, ClauseSerializer, ClauseRuleSerializer,
    ContractClauseSerializer
)


class ContractDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Contract`
    """
    name = "rea_contract"
    serializer_class = ContractSerializer


class ClauseDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Clause`
    """
    name = "rea_clause"
    serializer_class = ClauseSerializer


class ClauseRuleDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `ClauseRule`
    """
    name = "rea_clause_rule"
    serializer_class = ClauseRuleSerializer


class ContractClauseDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `ContractClause`
    """
    name = "rea_contract_clause"
    serializer_class = ContractClauseSerializer


mongodb.register(ContractDocumentCollection())
mongodb.register(ClauseDocumentCollection())
mongodb.register(ClauseRuleDocumentCollection())
mongodb.register(ContractClauseDocumentCollection())
