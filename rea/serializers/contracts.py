from rea.models.contracts import Contract, Clause, ClauseRule
from rea.serializers.core import REASerializer


class ContractSerializer(REASerializer):
    """
    Serializer for the `ContractContract` model
    """
    class Meta:
        model = Contract
        fields = (
            "id", "title", "short_title"
        )


class ClauseSerializer(REASerializer):
    """
    Serializer for the `Clause` model
    """
    class Meta:
        model = Clause
        fields = ( "id", )


class ClauseRuleSerializer(REASerializer):
    """
    Serializer for the `ClauseRule` model
    """
    clause = ClauseSerializer()

    class Meta:
        model = ClauseRule
        fields = (
            "id", "created_at", "created_by", "modified_at",
            "modified_by", "clause"
        )


class ContractClauseSerializer(REASerializer):
    """
    Serializer for the `ContractClause` model
    """
    contract = ContractSerializer()
    clause = ClauseSerializer()

    class Meta:
        model = ClauseRule
        fields = (
            "id", "contract", "clause"
        )
