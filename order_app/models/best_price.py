"""

"""
import logging
from decimal import Decimal

from django.db import models
from django.utils import timezone
from django.conf import settings


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class BestPrice(models.Model):
    """
    A model to keep the best sell and the best buy orders at lookup time.
    (time of observation, when API call was produced).

    Where:
     `raw_json` is a raw json response in binary representation,
     `hash_field` is a md5 hash, used for development purpose to make sure we
      don't duplicates of json data, should be removed in the future.

    Other fields are direct copies of JSON response keys.
    """
    best_sell = models.DecimalField(
        max_digits=12, decimal_places=8, null=False
    )
    best_buy = models.DecimalField(
        max_digits=12, decimal_places=8, null=False
    )
    last_price = models.DecimalField(
        max_digits=12, decimal_places=8, null=False
    )
    volume_24 = models.DecimalField(
        max_digits=14, decimal_places=8, null=False
    )
    lookup_time = models.DateTimeField("lookup time", default=timezone.now)
    sell_change = models.IntegerField()
    buy_change = models.IntegerField()
    hash_field = models.CharField(max_length=32)
    raw_json = models.BinaryField(max_length=32 * 1024)  # 32 KiB

    class Meta:
        """
        Return table records in descend order by their primary key when
        making ORM requests.
        """
        ordering = ["-id"]

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
        hash_field = self.hash_field

        return f"{local_time} {hash_field}"

    def get_hash_as_str(self) -> str:
        """Return `hash_field` represented as hexadecimal number."""
        return str(self.hash_field)

    def _get_change(self) -> tuple[Decimal, Decimal]:
        """
        Check if the best sell order and the best buy order has changed,
        if so return the difference between previous and current best sell
        and best buy orders.
        """
        # If this is the first record of the table, then there is nothing to
        # compare with so price change is zero
        if not self.id or self.id == 1:
            sell_change = Decimal("0.0")
            buy_change = Decimal("0.0")
        elif self.id > 1:
            # Get previous row
            prev_row = BestPrice.objects.get(id=self.id-1)
            sell_change = Decimal(self.best_sell) - Decimal(prev_row.best_sell)
            buy_change = Decimal(self.best_buy) - Decimal(prev_row.best_buy)

        return (sell_change, buy_change)

    def save(self, *args, **kwargs) -> None:
        """
        Calculate changing of the best sell/buy prices before saving a row.
        """
        self.sell_change, self.buy_change = self._get_change()
        super(BestPrice, self).save(*args, **kwargs)
