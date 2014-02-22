import logging

from django.db import models
from django_xworkflows import models as xwf_models

from entropy.base import (
    TextMixin, TitleMixin, CreatedMixin, ModifiedMixin, OrderingMixin
)

from cqrs.mongo import CQRSPolymorphicModel
from cqrs.noconflict import classmaker

from rea.settings import REA_RECEIVING_AGENT_MODEL, REA_PROVIDING_AGENT_MODEL


logger = logging.getLogger(__name__)


class Contract(CQRSPolymorphicModel, TitleMixin):
    '''
    Contract model which is instantiated by an Offer for Goods (Products) or Services
    in return for Payment or other form of Exchange Duality.
    '''

    # TODO:
    # Visitor Pattern Override
    # Versioning

    pass


class ContractInstance(xwf_models.WorkflowEnabled, CQRSPolymorphicModel):
    '''
    A completely instantiated instance of a contract that has become an
    immutable binding agreement between the participating Agents

    The Instance model gains the Workflow functions; whilst the Contract model
    is more an abstracta template.

    At time of intantiation a complete copy is made of the Contract
    '''

    __metaclass__ = classmaker()
    
    receiving_agent = models.ForeignKey(
        REA_RECEIVING_AGENT_MODEL,
        related_name='%(app_label)s_%(class)s_receiving_agent'
    )
    providing_agent = models.ForeignKey(
        REA_PROVIDING_AGENT_MODEL,
        related_name='%(app_label)s_%(class)s_providing_agent'
    )

    # XXX
    # Candidate methods
    # Visitor pattern

    def is_reciprocicated(self):
        return True

    def is_satisfied(self):
        return True
        # Loop through ordered Contract Clauses with their respective
        # Clause Rules.  If all pass, then the Contract is satisfied / fulfilled.
        # XXX implement logic.
        # XXX integrate with workflow states.


class Clause(CQRSPolymorphicModel, TitleMixin, TextMixin):
    '''
    A Clause is a reuseable set of one or more Clause Rules, attached
    by the ClauseRuleAspect pattern.

    '''

    # title
    # short_title
    pass


class ClauseRuleAspect(CQRSPolymorphicModel, CreatedMixin, ModifiedMixin):
    '''
    Attached to a Contract via through model ContractClause.  This model
    must be overridden with a provided `is_passing` method that returns True
    or False depending on the business logic required.

    '''

    # clause = models.ForeignKey(
    #     'Clause',
    #     related_name='%(app_label)s_%(class)s_clause'
    # )

    def is_passing(self):
        '''
        Test whether the current clause passes or fails. Returns
        either True or False.

        Usage:
            if clause_rule.is_passing:
                # do something...
        '''
        raise NotImplementedError(
            'Must override is_passing method for each rule')


class ContractClause(CQRSPolymorphicModel, OrderingMixin):
    '''
    Contract Clause
    
    '''
    # order / ordering

    contract = models.ForeignKey('Contract')
    clause = models.ForeignKey('Clause')


class ContractInstanceClause(CQRSPolymorphicModel, OrderingMixin):
    '''
    A full instantiated Contrace Instance Clause

    '''

    contract_instance = models.ForeignKey('ContractInstance')
    clause = models.ForeignKey('Clause')


# 
# Clause Rules Library
# 

class PaymentReceived(ClauseRuleAspect):

    def is_passing(self):
        return True
        # Logic here to determine whether a payment has been received.


class FulfilmentMade(ClauseRuleAspect):

    def is_passing(self):
        return True
        # Logic to determine the fulfilment of an Order