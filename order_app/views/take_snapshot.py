"""

"""
import logging

from django.http import HttpResponse

from order_app.models.order_snapshot import OrderSnapshot
from .fetch import fetch, validate_order_book


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def take_snapshot(request):
    """"""
    # orders_url = "https://www.occe.io/api/v2/public/orders/ltv_usdt"
    orders_url = "https://api.occe.io/public/orders/ltv_usdt"
    raw_snapshot = fetch(orders_url)
    if raw_snapshot is not None:
        snapshot = validate_order_book(raw_snapshot)
        if snapshot is None:
            logger.info("Line 108:")
        else:
            _hash = snapshot["_hash"]
            rows_count = OrderSnapshot.objects.count()
            if rows_count == 0:
                new_row = OrderSnapshot.objects.create(_hash=snapshot["_hash"],
                                                       data=snapshot["data"])
            elif rows_count > 0:
                last_snapshot = OrderSnapshot.objects.order_by("-lookup_time",
                                                               "-pk").first()
                last_hash = last_snapshot.hash_field
                if last_hash != _hash:
                    new_row = OrderSnapshot.objects.create(
                        _hash=snapshot["_hash"], data=snapshot["data"])
                else:
                    logger.info("Cannot create Snapshot coz last is the same")

        return HttpResponse("Good")  # TODO: Remove
