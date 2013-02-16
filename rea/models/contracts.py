from django.db import models

from polymorphic.polymorphic_model import PolymorphicModel

from entropy.base import SlugMixin, OrderingMixin, TitleMixin, TextMixin


class Contract(PolymorphicModel, TitleMixin, SlugMixin):

    class Meta:
        app_label = 'rea'


class Clause(TextMixin):

    class Meta:
        app_label = 'rea'


class ClauseRule(OrderingMixin):

    clause = models.ForeignKey(
        'Clause')

    class Meta:
        app_label = 'rea'


class ContractClause(PolymorphicModel):

    contract = models.ForeignKey(
        'Contract')

    clause = models.ForeignKey(
        'Clause')

    class Meta:
        app_label = 'rea'