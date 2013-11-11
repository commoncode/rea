from rea.mongo import mongodb, DRFDocumentCollection
from rea.models.resources import Resource


class ResourceDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Resource`
    """
    serializer_class = "rea.serializers.resources.ResourceSerializer"
    model = Resource
    name = "resource"


mongodb.register(ResourceDocumentCollection())
