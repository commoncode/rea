from django.db import models
from polymorphic.polymorphic_model import PolymorphicModel

from entropy.base import SlugMixin, TitleMixin


class Resource(PolymorphicModel, TitleMixin, SlugMixin):

    class Meta:
        app_label = "rea"