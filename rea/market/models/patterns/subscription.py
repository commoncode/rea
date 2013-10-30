import datetime
from django.db import models
from django_xworkflows import models as xwf_models
from django.utils.translation import ugettext_lazy as _

from rea.models.contracts import Contract, Clause
from rea.market.models.agents import Customer, Enterprise
from rea.market.rules import DateAtLeastRule


class SubscriptionWorkflow(xwf_models.Workflow):
    """
    States of a subscription based transaction
    """
    states = (
        ('wait', _(u"Wait for Payment")),
        ('recieve', _(u"Recieved a Payment")),
        ('missed', _(u"Missed a Payment")),
    )

    transitions = (
        ('recieved_payment', 'wait', 'recieve'),
        ('missed_payment', 'wait', 'missed'),
        ('return_to_wait', 'missed', 'wait'),
        ('return_to_wait', 'recieve', 'wait'),
    )

    initial_state = 'wait'


class SubscriptionClause(Clause):

    def save(self, *args, **kwargs):
        create_rules = False
        if not self.pk:
            create_rules = True
        super(SubscriptionClause, self).save(*args, **kwargs)

        if create_rules:
            now = datetime.datetime.now()
            DateAtLeastRule.objects.create(date=now, clause=self)

    class Meta:
        app_label = 'market'


class SubscriptionContract(Contract):
    """
    A product subscription contract.

    Contains a list of clauses that must be satisfied for
    state continuation.
    """
    state = xwf_models.StateField(SubscriptionWorkflow)

    customer = models.ForeignKey(Customer)
    enterprise = models.ForeignKey(Enterprise)

    def get_current_state(self):
        return self.state.state.name

    class Meta:
        abstract = True
        app_label = 'market'
