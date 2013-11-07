from entropy.base import CreatedMixin
from rea.models.reciprocity import Reciprocity


class LedgerLine(Reciprocity, CreatedMixin):
    """
    Record of an exchange of resources
    """
    class Meta:
        app_label = "market"
