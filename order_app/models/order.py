"""

"""
from django.db import models
from django.utils import timezone
from django.conf import settings


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
        """
        `unique_together` setting supposed to protect the table from record
        duplication.
        """
        abstract = True
        unique_together = (
            ("amount", "date", "label", "order_id", "price", "total"),
        )

    def __str__(self) -> str:
        """
        A verbose name of a separate order is a combination of `amount` of
        coins offered to trade, at given `price` and datetime the order was
        placed translated to local timezone.

        :return: `[3.0 Coins @ 0.0002 [20.12.2021 15:50:20]`
        """
        local_date = timezone.localtime(self.date).strftime(
            settings.U_DATETIME_FORMAT
        )
        price = int(self.price)
        return f"{self.amount} Coins @ {price} [{local_date}]"


class BuyOrder(Order):
    """
    A table that contains only buy orders. This is a silly attempt to
    implement database normalization or partitioning, I can't remember by now.
    """
    pass


class SellOrder(Order):
    """
    A table that contains only sell orders .This is a silly attempt to
    implement database normalization or partitioning, I can't remember by now.
    """
    pass
