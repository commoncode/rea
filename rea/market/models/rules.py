import logging
from django.db import models
from rea.mongo import mongodb
from rea.models.contracts import ClauseRule
from rea.collections.contracts import ClauseRuleDocumentCollection

logger = logging.getLogger(__name__)


###########################################################
#  Django Models                                          #
###########################################################


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
        app_label = "market"


###########################################################
#  Denormalize Document Collections                       #
###########################################################


class DateAtLeastRuleDocumentCollection(ClauseRuleDocumentCollection):
    """
    A denormalized collection of `DateAtLeastRule`
    """
    model = DateAtLeastRule
    name = "market_date_at_least_rule"


###########################################################
#  Mongodb registers                                      #
###########################################################


mongodb.register(DateAtLeastRuleDocumentCollection())

