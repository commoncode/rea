import logging
from django.db import models
from django_xworkflows import models as xwf_models

from entropy.base import TitleMixin, CreatedMixin, ModifiedMixin
from rea.noconflict import classmaker
from rea.models.core import REAModel

logger = logging.getLogger(__name__)


class Order(REAModel, CreatedMixin, ModifiedMixin):
    """
    TODO: Move this to market?
    """
    # True if all contracts are accepted
    agent = models.ForeignKey("rea.Agent")

    class Meta:
        app_label = "rea"


class Contract(xwf_models.WorkflowEnabled, REAModel, TitleMixin):
    """
    """
    __metaclass__ = classmaker()

    order = models.ForeignKey(Order)

    class Meta:
        app_label = 'rea'


class Clause(REAModel):
    """
    """
    class Meta:
        app_label = "rea"


class ClauseRule(REAModel, CreatedMixin, ModifiedMixin):

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


class ContractClause(REAModel):
    """
    """
    contract = models.ForeignKey('Contract')
    clause = models.ForeignKey('Clause', null=True,
        related_name="%(class)s_set")

    class Meta:
        app_label = "rea"
