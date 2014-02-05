from entropy.base import SlugMixin, TitleMixin

from .core import REAModel


class Agent(REAModel, TitleMixin):

    class Meta:
        app_label = "rea"
