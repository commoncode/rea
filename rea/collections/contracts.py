from rea.mongo import mongodb, DRFDocumentCollection
from rea.models.contracts import Contract, Clause, ClauseRule, ContractClause


class ContractDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Contract`
    """
    name = "contract"
    model = Contract
    serializer_class = "rea.serializers.contracts.ContractSerializer"


class ClauseDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Clause`
    """
    name = "clause"
    model = Clause
    serializer_class = "rea.serializers.contracts.ClauseSerializer"


class ClauseRuleDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `ClauseRule`
    """
    name = "clause_rule"
    model = ClauseRule
    serializer_class = "rea.serializers.contracts.ClauseRuleSerializer"


class ContractClauseDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `ContractClause`
    """
    name = "contract_clause"
    model = ContractClause
    serializer_class = "rea.serializers.contracts.ContractClauseSerializer"


mongodb.register(ContractDocumentCollection())
mongodb.register(ClauseDocumentCollection())
mongodb.register(ClauseRuleDocumentCollection())
mongodb.register(ContractClauseDocumentCollection())
