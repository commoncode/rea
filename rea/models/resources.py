from entropy.base import SlugMixin, TitleMixin
from cqrs.mongo import CQRSPolymorphicModel


class Resource(CQRSPolymorphicModel, TitleMixin, SlugMixin):
	pass
