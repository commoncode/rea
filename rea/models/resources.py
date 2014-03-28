from entropy.base import SlugMixin, TitleMixin
from cqrs.models import CQRSPolymorphicModel


class Resource(CQRSPolymorphicModel, TitleMixin, SlugMixin):
	pass
