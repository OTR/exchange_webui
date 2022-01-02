"""

"""
import json
import logging

from importlib import import_module
from django.conf import settings
from django.views.generic import TemplateView

from services.fetch import fetch, format_orders


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
PUBLIC_API_CONF = import_module(f"{settings.U_USE_EXCHANGE}.public_api")


class ActiveOrderView(TemplateView):
    """
    A view to display Active Orders placed in an order book by given trade pair.
    """
    template_name = "order_app/active_orders.html"

    def get_context_data(self, **kwargs) -> dict:
        """TODO: move JSON parsing into services module."""
        context = super().get_context_data(**kwargs)
        pattern = PUBLIC_API_CONF.ACTIVE_ORDERS_URL_PATTERN
        orders_url = pattern.format(pair="ltv_usdt")
        data = fetch(orders_url)
        if data is None:
            LOGGER.info("Fetcher returned None")
            return {}
        else:
            json_obj = json.loads(data)
            if json_obj["result"] == "success":
                buy_orders = json_obj["data"]["buyOrders"]
                sell_orders = json_obj["data"]["sellOrders"]

                formatted_sell_orders = format_orders(
                    sell_orders,
                    is_buy_order=False
                )
                formatted_buy_orders = format_orders(
                    buy_orders,
                    is_buy_order=True
                )

                context = {
                    "sellbuy_orders": {
                        "sell_orders": formatted_sell_orders,
                        "buy_orders": formatted_buy_orders
                    },
                    "bar": False
                }

            return context
