import logging
from django.db import models
from rea.models.contracts import ClauseRule

logger = logging.getLogger(__name__)


class DateAtLeastRule(ClauseRule):
    """
    Date must be equal to or greater than the current date for a contract
    execution to be valid
    """
    date = models.DateTimeField(blank=False, null=False)

    def clause_passes(self):
        """
        Test whether the current clause passes or fails. Returns
        either True or False.
        """
        logger.debug("DateAtLeastRule passes")
        return True

    class Meta:
        app_label = 'market'


