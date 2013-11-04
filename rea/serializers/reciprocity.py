from rea.models.reciprocity import Increment, Decrement, Reciprocity
from rea.serializers.core import REASerializer
from rea.serializers.commitments import CommitmentSerializer


class ReciprocitySerializer(REASerializer):
    """
    Serializer for the `Event` model
    """
    related_commitment = CommitmentSerializer()

    class Meta:
        model = Reciprocity
        fields = (
            "id", "increment", "decrement"
        )


class IncrementSerializer(REASerializer):
    """
    Serializer for the `Increment` model
    """
    class Meta:
        model = Increment
        fields = ( "id", )


class DecrementSerializer(REASerializer):
    """
    Serializer for the `Decrement` model
    """
    class Meta:
        model = Decrement
        fields = ( "id", )

