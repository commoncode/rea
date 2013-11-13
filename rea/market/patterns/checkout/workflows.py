from django_xworkflows import models as xwf_models
from django.utils.translation import ugettext_lazy as _


class CheckoutWorkflow(xwf_models.Workflow):
    """
    States of a checkout based transaction
    """
    states = (
        # Our initial state
        ('init', _(u"Initial State")),
        # New commitment to pay within 30 days
        ('commitment', _(u"Committed to pay for checkout")),
        # The event of exchanging resources
        ('event', _(u"Payment recieved")),
    )

    transitions = (
        ('customer_committed', ('init'), 'commitment'),
        ('payment_recieved', 'commitment', 'event'),
    )

    initial_state = 'init'
