from entropy.base import SlugMixin, TitleMixin

from cqrs.models import CQRSPolymorphicModel


class Agent(CQRSPolymorphicModel, SlugMixin, TitleMixin):
	pass
