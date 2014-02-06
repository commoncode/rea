from django.db import models

from cqrs.mongo import CQRSPolymorphicModel


class LineMixin(CQRSPolymorphicModel):
    """
    Mixin for Increment and Decrement lines
    """
    providing_agent = models.ForeignKey('Agent',
        related_name='%(app_label)s_%(class)s_providing_agents')
    recieving_agent = models.ForeignKey('Agent',
        related_name='%(app_label)s_%(class)s_recieving_agents')

    resource = models.ForeignKey('Resource')
    quantity = models.FloatField()

    class Meta:
        app_label = "rea"
        abstract = True


from .events import *
from .contracts import *
from .agents import *
from .commitments import *
from .resources import *
