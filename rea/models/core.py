from django.db import models
from bson.objectid import ObjectId
from polymorphic.polymorphic_model import PolymorphicModel


class REAModel(PolymorphicModel):

    mongoID = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.mongoID:
            self.mongoID = str(ObjectId())
        super(REAModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
