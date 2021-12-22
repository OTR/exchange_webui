"""

"""
import json
import logging
from datetime import datetime

from django.db import models
from django.utils import timezone

from ..models import BuyOrder, OrderBookState, SellOrder


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class OrderSnapshot(models.Model):
    """
    `hash_field` - there must be only one instance for a certain hash
     otherwise we have a duplicate
    """
    # lookup_time = models.DateTimeField("lookup time", auto_now_add=True)
    lookup_time = models.DateTimeField("lookup time", default=timezone.now)
    hash_field = models.CharField(max_length=32)
    data = models.BinaryField(max_length=32 * 1024)  # 32 Kb

    def __str__(self):
        """"""
        local_time = timezone.localtime(self.lookup_time).strftime(
            "%d.%m.%Y %H:%M:%S"
        )
        return "{} {}".format(local_time, self.hash_field)

    def hash_as_hex(self):
        """Return _hash field represented as hexadecimal representation."""
        return self.hash_field

    class Meta:
        """"""
        ordering = ["-id"]

    def data_as_string(self):
        """Return data (JSON response) as string."""
        return self.data.decode("UTF-8")

    def save(self, *args, **kwargs):
        """"""
        json_obj = json.loads(self.data)
        buy_orders = json_obj["buyOrders"]
        sell_orders = json_obj["sellOrders"]
        state, is_created = OrderBookState.objects.get_or_create(
            lookup_time=self.lookup_time
        )
        if is_created:
            for order_type, _set in (("sell", sell_orders), ("buy", buy_orders)):
                for row in _set:
                    date_as_int = float(
                        "{}.{}".format(row["date"][:10], row["date"][10:]))
                    date = datetime.fromtimestamp(date_as_int)
                    if order_type == "sell":
                        use_model = SellOrder
                    else:
                        use_model = BuyOrder
                    obj, is_created = use_model.objects.get_or_create(
                        amount=row["amount"],
                        date=date,
                        label=row["label"],
                        order_id=row["orderId"],
                        price=row["price"],
                        total=row["total"])
                    if is_created:
                        if order_type == "sell":
                            state.sell_orders.add(obj)
                        else:
                            state.buy_orders.add(obj)
                    else:
                        LOGGER.info("Cannot create Order coz already is_created")
        else:
            LOGGER.info(
                "Cannot create a row because a row with given look up time "
                "is already created"
            )

        super().save(*args, **kwargs)
