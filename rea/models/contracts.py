import logging
from django.db import models
from django_xworkflows import models as xwf_models

from polymorphic.polymorphic_model import PolymorphicModel
from entropy.base import TitleMixin, CreatedMixin, ModifiedMixin

from rea.noconflict import classmaker

logger = logging.getLogger(__name__)


class Contract(xwf_models.WorkflowEnabled, PolymorphicModel, TitleMixin):

    __metaclass__ = classmaker()

    class Meta:
        app_label = 'rea'


class Clause(PolymorphicModel):

    class Meta:
        app_label = "rea"


class ClauseRule(PolymorphicModel, CreatedMixin, ModifiedMixin):

    clause = models.ForeignKey('Clause',
        related_name="%(class)s_set")

    def clause_passes(self):
        """
        Test whether the current clause passes or fails. Returns
        either True or False.
        """
        raise NotImplementedError(
            "Must override clause_passes method for each rule")

    class Meta:
        app_label = "rea"


class ContractClause(PolymorphicModel):

    contract = models.ForeignKey('Contract')
    clause = models.ForeignKey('Clause', null=True,
        related_name="%(class)s_set")

    class Meta:
        app_label = "rea"
