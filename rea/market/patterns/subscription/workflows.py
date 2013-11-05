from django_xworkflows import models as xwf_models
from django.utils.translation import ugettext_lazy as _


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
