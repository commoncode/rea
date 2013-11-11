from django.db import models
from rea.models.agents import Agent


class Customer(Agent):
    """
    A customer agent (buyer)
    """
    date_joined = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        app_label = 'market'


class Enterprise(Agent):
    """
    An enterprise agent (seller)
    """
    class Meta:
        app_label = 'market'
