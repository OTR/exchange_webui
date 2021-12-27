"""

"""
from django.db import models
from django.utils import timezone


class Order(models.Model):
    """
    A base class for both Buy and Sell orders. Needed to separate orders
    by their type into two tables to provide database normalization.
    """
    amount = models.DecimalField(max_digits=14, decimal_places=8)
    date = models.DateTimeField()
    label = models.CharField(max_length=127)
    order_id = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=8)
    total = models.DecimalField(max_digits=12, decimal_places=8)

    class Meta:
        """"""
        abstract = True
        unique_together = (
            ("amount", "date", "label", "order_id", "price", "total"),
        )

    def __str__(self):
        """"""
        local_date = timezone.localtime(self.date).strftime("%d.%m.%Y %H:%M:%S")
        price = int(self.price)
        return f"{self.amount} Coins @ {price} [{local_date}]"


class BuyOrder(Order):
    """"""
    pass


class SellOrder(Order):
    """"""
    pass
