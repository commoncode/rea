from django.db import models
from bson.objectid import ObjectId
from polymorphic.polymorphic_model import PolymorphicModel


class REAModel(PolymorphicModel):
    """
    This model allows rea-serializer plugins to be effective by
    assigning mongoID.

    XXX in the case of a non-mongo architecture; this would need
    to be optioned out.
    """

    mongoID = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.mongoID:
            self.mongoID = str(ObjectId())
        super(REAModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
