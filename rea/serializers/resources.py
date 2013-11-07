from rea.serializers.core import REASerializer
from rea.models.resources import Resource


class ResourceSerializer(REASerializer):
    """
    Serializer for the `Resource` model
    """
    class Meta:
        model = Resource
        fields = ( "id", "title" )

