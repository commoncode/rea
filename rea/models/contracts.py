import logging
from django.db import models
from django_xworkflows import models as xwf_models

from denormalize.models import DocumentCollection
from polymorphic.polymorphic_model import PolymorphicModel
from entropy.base import TitleMixin, CreatedMixin, ModifiedMixin
from rea.mongo import mongodb
from rea.noconflict import classmaker

logger = logging.getLogger(__name__)


###########################################################
#  Django Models                                          #
###########################################################


class Contract(xwf_models.WorkflowEnabled, PolymorphicModel, TitleMixin):
    """
    """
    __metaclass__ = classmaker()

    class Meta:
        app_label = 'rea'


class Clause(PolymorphicModel):
    """
    """
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
        logger.error("Not working, damn it...")
        return True
        # raise NotImplementedError(
        #     "Must override clause_passes method for each rule")

    class Meta:
        app_label = "rea"


class ContractClause(PolymorphicModel):
    """
    """
    contract = models.ForeignKey('Contract')
    clause = models.ForeignKey('Clause', null=True,
        related_name="%(class)s_set")

    class Meta:
        app_label = "rea"


###########################################################
#  Denormalize Document Collections                       #
###########################################################


class ContractDocumentCollection(DocumentCollection):
    """
    A denormalized collection of `Contract`
    """
    model = Contract
    name = "rea_contract"
    exclude_all = ['state']


class ClauseDocumentCollection(DocumentCollection):
    """
    A denormalized collection of `Clause`
    """
    model = Clause
    name = "rea_clause"
    exclude_all = ['state']


class ClauseRuleDocumentCollection(DocumentCollection):
    """
    A denormalized collection of `ClauseRule`
    """
    model = ClauseRule
    name = "rea_clause_rule"
    select_related = ['clause']
    exclude_all = ['state']


class ContractClauseDocumentCollection(DocumentCollection):
    """
    A denormalized collection of `ContractClause`
    """
    model = ContractClause
    name = "rea_contract_clause"
    select_related = ['contract', 'clause']
    exclude_all = ['state']


###########################################################
#  Mongodb registers                                      #
###########################################################


mongodb.register(ContractDocumentCollection())
mongodb.register(ClauseDocumentCollection())
mongodb.register(ClauseRuleDocumentCollection())
mongodb.register(ContractClauseDocumentCollection())
