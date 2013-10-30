from polymorphic.polymorphic_model import PolymorphicModel
from entropy.base import SlugMixin, TitleMixin


class Agent(PolymorphicModel, TitleMixin, SlugMixin):

    class Meta:
        app_label = "rea"