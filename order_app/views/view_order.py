"""

"""
import json
import logging

from django.views.generic import TemplateView

from .fetch import fetch, format_orders


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class OrderView(TemplateView):
    """"""
    template_name = "order_app/orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # url = "https://www.occe.io/api/v2/public/orders/ltv_usdt"
        url = "https://api.occe.io/public/orders/ltv_usdt"
        data = fetch(url)
        if data is None:
            logger.info("Fetcher returned None")
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

            else:
                logger.info("JSON is not succeed")
                return {}
