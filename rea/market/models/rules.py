from django.db import models
from rea.models.contracts import ClauseRule


class DateAtLeastRule(ClauseRule):
    """
    Date must be equal to or greater than the current date for a contract
    execution to be valid
    """
    date = models.DateTimeField(blank=False, null=False)

    class Meta:
        app_label = 'market'


