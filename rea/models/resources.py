from entropy.base import SlugMixin, TitleMixin
from rea.models.core import REAModel


class Resource(REAModel, TitleMixin, SlugMixin):

    class Meta:
        app_label = "rea"
