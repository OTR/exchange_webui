"""

"""
from django.db import models


class FaucetAddress(models.Model):
    """"""
    address = models.CharField(max_length=64, unique=True)
    balance = models.IntegerField()

    def __str__(self):
        """"""
        return self.address
