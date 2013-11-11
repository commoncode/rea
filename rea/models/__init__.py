from rea.models.core import REAModel
from django.db import models

class LineMixin(REAModel):
    """
    Mixin for Increment and Decrement lines
    """
    providing_agent = models.ForeignKey('Agent',
        related_name='%(app_label)s_%(class)s_providing_agents')
    recieving_agent = models.ForeignKey('Agent',
        related_name='%(app_label)s_%(class)s_recieving_agents')

    resource = models.ForeignKey('Resource')
    quantity = models.PositiveIntegerField()

    class Meta:
        app_label = "rea"
        abstract = True


from .events import *
from .contracts import *
from .agents import *
from .commitments import *
from .resources import *
