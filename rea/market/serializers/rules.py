from rea.serializers.contracts import ClauseRuleSerializer
from rea.market.models.rules import DateAtLeastRule


class DateAtLeastRuleSerializer(ClauseRuleSerializer):
    """
    Serializer for the `DateAtLeastRule` model
    """
    class Meta(ClauseRuleSerializer.Meta):
        model = DateAtLeastRule
