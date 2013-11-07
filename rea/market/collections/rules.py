from rea.collections.contracts import ClauseRuleDocumentCollection
from rea.market.serializers.rules import DateAtLeastRuleSerializer
from rea.mongo import mongodb, DRFDocumentCollection


class DateAtLeastRuleDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `DateAtLeastRule`
    """
    parent_collection = ClauseRuleDocumentCollection
    serializer_class = DateAtLeastRuleSerializer
    name = "dateatleast_rule"


mongodb.register(DateAtLeastRuleDocumentCollection())
