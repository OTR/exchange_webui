"""

"""
from django.db import models


class FaucetAddress(models.Model):
    """Not Implemented yet."""
    address = models.CharField(max_length=64, unique=True)
    balance = models.IntegerField()

    def __str__(self) -> str:
        """Return user address as verbose name."""
        return self.address
