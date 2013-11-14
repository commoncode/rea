from rea.models.contracts import Contract, Clause, ClauseRule, Order
from rea.serializers.core import REASerializer
from rest_framework import serializers


class OrderSerializer(REASerializer):
    """
    Serializer for the `Order` model
    """
    agent = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Order
        fields = (
            "id", "created_at", "created_by", "agent"
        )


class ContractSerializer(REASerializer):
    """
    Serializer for the `ContractContract` model
    """
    order = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Contract
        fields = (
            "id", "title", "short_title", "order"
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
