from .events import Event


class Payment(Event):

    class Meta:
        app_label = 'rea'