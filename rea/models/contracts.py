from django.db import models

from polymorphic.polymorphic_model import PolymorphicModel

from entropy.base import SlugMixin, OrderableRuleMixin, TitleMixin, TextMixin


class Contract(PolymorphicModel, TitleMixin, SlugMixin):

    class Meta:
        app_label = 'rea'


class Clause(TextMixin):

    contract = models.ForeignKey(
        'Contract')

    class Meta:
        app_label = 'rea'


class ClauseRule(OrderableRuleMixin):

    clause = models.ForeignKey(
        'Clause')

    class Meta:
        app_label = 'rea'