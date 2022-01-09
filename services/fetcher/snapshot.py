"""

"""
import logging
from importlib import import_module

from django.conf import settings

from order_app.models.active_orders_raw_json import ActiveOrdersRawJSON
from services.fetcher.fetch import fetch, validate_order_book

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

PUBLIC_API_CONF = import_module(f"{settings.U_USE_EXCHANGE}.public_api")


def take_active_orders_snapshot():
    """"""
    pattern = PUBLIC_API_CONF.ACTIVE_ORDERS_URL_PATTERN
    orders_url = pattern.format(
        pair=PUBLIC_API_CONF.TRADE_PAIR
    )
    raw_snapshot = fetch(orders_url)
    if raw_snapshot is not None:
        snapshot = validate_order_book(raw_snapshot)
        if snapshot is None:
            LOGGER.info("Validate returned None")
        else:
            _hash = snapshot["_hash"]
            rows_count = ActiveOrdersRawJSON.objects.count()
            if rows_count == 0:
                new_row = ActiveOrdersRawJSON.objects.create(
                    hash_field=snapshot["_hash"],
                    data=snapshot["data"]
                )
            elif rows_count > 0:
                last_snapshot = ActiveOrdersRawJSON.objects.order_by(
                    "-lookup_time", "-pk"
                ).first()
                last_hash = last_snapshot.hash_field
                if last_hash != _hash:
                    new_row = ActiveOrdersRawJSON.objects.create(
                        hash_field=snapshot["_hash"],
                        data=snapshot["data"]
                    )
                else:
                    LOGGER.info("Cannot create Snapshot coz last is the same")
