from django_xworkflows import models as xwf_models
from django.utils.translation import ugettext_lazy as _


class VIPWorkflow(xwf_models.Workflow):
    """
    States of a subscription based transaction
    """
    states = (
        # Our initial state
        ('init', _(u"Initial State")),
        # New commitment to pay within 30 days
        ('commitment', _(u"Committed to pay for VIP membership")),
        # The event of exchanging resources
        ('event', _(u"Payment recieved")),
    )

    transitions = (
        ('create_commitment', ('init', 'event'), 'commitment'),
        ('payment_recieved', 'commitment', 'event'),
    )

    initial_state = 'init'
