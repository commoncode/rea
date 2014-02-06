import logging

from django.db import models
from django_xworkflows import models as xwf_models

from entropy.base import TitleMixin, CreatedMixin, ModifiedMixin

from ..noconflict import classmaker
from cqrs.mongo import CQRSPolymorphicModel


logger = logging.getLogger(__name__)


class Contract(xwf_models.WorkflowEnabled, CQRSPolymorphicModel, TitleMixin):
    """
    """
    __metaclass__ = classmaker()

    class Meta:
        app_label = 'rea'


class Clause(CQRSPolymorphicModel):
    """
    """
    class Meta:
        app_label = "rea"


class ClauseRule(CQRSPolymorphicModel, CreatedMixin, ModifiedMixin):

    clause = models.ForeignKey('Clause',
        related_name="%(class)s_set")

    def clause_passes(self):
        """
        Test whether the current clause passes or fails. Returns
        either True or False.
        """
        logger.error("Not working, damn it...")
        return True
        # raise NotImplementedError(
        #     "Must override clause_passes method for each rule")

    class Meta:
        app_label = "rea"


class ContractClause(CQRSPolymorphicModel):
    """
    """
    contract = models.ForeignKey('Contract')
    clause = models.ForeignKey('Clause', null=True,
        related_name="%(class)s_set")

    class Meta:
        app_label = "rea"
