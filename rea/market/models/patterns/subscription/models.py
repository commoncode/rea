import datetime
from django.db import models
from rea.models.contracts import Clause
from rea.market.models.rules import DateAtLeastRule
from rea.models.contracts import Contract
from django_xworkflows import models as xwf_models
from rea.market.models.patterns.subscription import SubscriptionWorkflow


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

    customer = models.ForeignKey('market.Customer')
    enterprise = models.ForeignKey('market.Enterprise')

    def get_current_state(self):
        return self.state.state.name

    class Meta:
        abstract = True
        app_label = 'market'
