"""

"""
import logging

from django.conf import settings
from importlib import import_module
from order_app.models.order_snapshot import OrderSnapshot
from services.fetch import fetch, validate_order_book


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

PUBLIC_API_CONF = import_module(f"{settings._USE_EXCHANGE}.public_api")


def take_snapshot():
    """"""
    pattern = PUBLIC_API_CONF.ACTIVE_ORDERS_URL_PATTERN
    orders_url = pattern.format(pair="ltv_usdt")
    raw_snapshot = fetch(orders_url)
    if raw_snapshot is not None:
        snapshot = validate_order_book(raw_snapshot)
        if snapshot is None:
            logger.info("Line 108:")
        else:
            _hash = snapshot["_hash"]
            rows_count = OrderSnapshot.objects.count()
            if rows_count == 0:
                new_row = OrderSnapshot.objects.create(
                    hash_field=snapshot["_hash"],
                    data=snapshot["data"]
                )
            elif rows_count > 0:
                last_snapshot = OrderSnapshot.objects.order_by("-lookup_time",
                                                               "-pk").first()
                last_hash = last_snapshot.hash_field
                if last_hash != _hash:
                    new_row = OrderSnapshot.objects.create(
                        hash_field=snapshot["_hash"],
                        data=snapshot["data"]
                    )
                else:
                    logger.info("Cannot create Snapshot coz last is the same")
