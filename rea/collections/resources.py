from rea.mongo import mongodb, DRFDocumentCollection
from rea.serializers.resources import ResourceSerializer


class ResourceDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Resource`
    """
    serializer_class = ResourceSerializer
    name = "rea_resource"


mongodb.register(ResourceDocumentCollection())
