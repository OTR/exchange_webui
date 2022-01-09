"""

"""
import json
import logging
from datetime import datetime
from decimal import Decimal

from django.db import models
from django.utils import timezone
from django.conf import settings

from order_app.models import BuyOrder, OrderBookState, SellOrder


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class ActiveOrdersRawJSON(models.Model):
    """
    `hash_field` - there must be only one instance for a certain hash
     otherwise we have a duplicate
    """
    lookup_time = models.DateTimeField("lookup time", default=timezone.now)
    hash_field = models.CharField(max_length=32)
    raw_json = models.BinaryField(max_length=32 * 1024)  # 32 KiB

    def __str__(self) -> str:
        """
        Verbose name of a database record to display in Django admin site.
        Consists of `lookup_time` (the moment at which API request was produced)
        and a `hash_field` which is a result of md5 hashing function over
        a raw JSON response.
        """
        local_time = timezone.localtime(self.lookup_time).strftime(
            settings.U_DATETIME_FORMAT
        )
        return "{} {}".format(local_time, self.hash_field)

    def hash_as_hex(self) -> str:
        """Return _hash field represented as hexadecimal representation."""
        return self.hash_field

    class Meta:
        """
        Return table records in descend order by their primary key when
        making ORM requests.
        """
        ordering = ["-id"]

    def data_as_string(self) -> str:
        """Return data (JSON response) as string."""
        return self.raw_json.decode("UTF-8")

    def save(self, *args, **kwargs) -> None:
        """"""
        json_obj = json.loads(self.raw_json)
        buy_orders = json_obj["data"]["buyOrders"]
        sell_orders = json_obj["data"]["sellOrders"]
        state, is_created = OrderBookState.objects.get_or_create(
            lookup_time=self.lookup_time
        )
        if is_created:
            for order_type, _set in (("sell", sell_orders), ("buy", buy_orders)):
                for row in _set:
                    json_date = row.get("date", 0)  # FIXME: a hack, API is not
                    # consistent
                    quotient, reminder = divmod(json_date, 1000)
                    date_as_float = float(
                        "{}.{}".format(quotient, reminder)
                    )
                    date = datetime.fromtimestamp(date_as_float)
                    if order_type == "sell":
                        use_model = SellOrder
                    else:
                        use_model = BuyOrder
                    obj, is_created = use_model.objects.get_or_create(
                        amount=Decimal(str(row["amount"])),
                        date=date,
                        label="",  # FIXME:
                        order_id=0,  # Fields from v2 API
                        price=Decimal(str(row["price"])),
                        total=Decimal(str(row["total"])))
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
