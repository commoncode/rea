from rea.models.agents import Agent


class Customer(Agent):
    """
    A customer agent (buyer)
    """
    class Meta:
        app_label = 'market'


class Enterprise(Agent):
    """
    An enterprise agent (seller)
    """
    class Meta:
        app_label = 'market'
