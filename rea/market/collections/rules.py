from rea.collections.contracts import ClauseRuleDocumentCollection
from rea.market.serializers.rules import DateAtLeastRuleSerializer
from rea.mongo import mongodb


class DateAtLeastRuleDocumentCollection(ClauseRuleDocumentCollection):
    """
    A denormalized collection of `DateAtLeastRule`
    """
    serializer_class = DateAtLeastRuleSerializer
    name = "market_date_at_least_rule"


mongodb.register(DateAtLeastRuleDocumentCollection())
