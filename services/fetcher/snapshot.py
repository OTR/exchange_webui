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
        curr_snapshot = validate_order_book(raw_snapshot)
        if curr_snapshot is None:
            LOGGER.info("Validate returned None")
        else:
            curr_hash = curr_snapshot["hash_field"]
            rows_count = ActiveOrdersRawJSON.objects.count()
            if rows_count == 0:
                new_row = ActiveOrdersRawJSON.objects.create(
                    hash_field=curr_snapshot["hash_field"],
                    raw_json=curr_snapshot["raw_json"]
                )
            elif rows_count > 0:
                prev_snapshot = ActiveOrdersRawJSON.objects.order_by(
                    "-lookup_time", "-pk"
                ).first()
                prev_hash = prev_snapshot.hash_field
                if prev_hash != curr_hash:
                    new_row = ActiveOrdersRawJSON.objects.create(
                        hash_field=curr_snapshot["hash_field"],
                        raw_json=curr_snapshot["raw_json"]
                    )
                else:
                    LOGGER.info("Cannot create Snapshot coz last is the same")
