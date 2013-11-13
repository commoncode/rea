from django.db import models
from rea.models.contracts import Contract
from django_xworkflows import models as xwf_models
from rea.market.patterns.salesorder.workflows import SalesOrderWorkflow


class SalesOrderContract(Contract):
    """
    A product subscription contract.

    Contains a list of clauses that must be satisfied for
    state continuation.
    """
    state = xwf_models.StateField(SalesOrderWorkflow)

    customer = models.ForeignKey('market.Customer')
    enterprise = models.ForeignKey('market.Enterprise')

    class Meta:
        abstract = True
        app_label = 'market'
