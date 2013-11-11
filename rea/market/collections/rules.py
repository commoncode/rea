from rea.collections.contracts import ClauseRuleDocumentCollection
from rea.mongo import mongodb, DRFDocumentCollection
from rea.market.models.rules import DateAtLeastRule


class DateAtLeastRuleDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `DateAtLeastRule`
    """
    parent_collection = ClauseRuleDocumentCollection
    model = DateAtLeastRule
    serializer_class = "rea.market.serializers.rules.DateAtLeastRuleSerializer"
    name = "dateatleast_rule"


mongodb.register(DateAtLeastRuleDocumentCollection())
