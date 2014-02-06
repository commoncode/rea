from entropy.base import SlugMixin, TitleMixin

from cqrs.mongo import CQRSPolymorphicModel


class Agent(CQRSPolymorphicModel, TitleMixin):

    class Meta:
        app_label = "rea"
