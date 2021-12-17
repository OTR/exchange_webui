"""

"""
import datetime
import json
import logging
from urllib import error
from urllib.request import urlopen

from django.shortcuts import render
from django.views.generic import TemplateView

from services.fetch import fetch, format_orders

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class OrderView(TemplateView):
    """"""
    template_name = "order_app/orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # url = "https://www.occe.io/api/v2/public/orders/ltv_usdt"
        url = "https://api.occe.io/public/orders/ltv_usdt"
        data = fetch(url)
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


def orders_view(request):
    """"""
    sell_orders, buy_orders = get_public_orders()

    formatted_sell_orders = _format_orders(sell_orders, is_buy=False)
    formatted_buy_orders = _format_orders(buy_orders, is_buy=True)

    context = {
        "sellbuy_orders": {
            "sell_orders": formatted_sell_orders,
            "buy_orders": formatted_buy_orders
        }
    }

    return render(request, "order_app/order_app.html", context)


def _format_orders(orders, is_buy=False):
    """Take orders class json object."""
    formatted_orders = []
    new_orders = []
    orders = sorted(orders,
                    key=lambda order: float(order["price"]),
                    reverse=is_buy
                    )
    # (  order["price"], , ) #
    total_cap = 0.0
    temp_cap = 0.0
    take = 10

    for index, order in enumerate(orders):
        if index < take:
            total_cap += float(order["total"])

    for index, order in enumerate(orders):
        if index < take:
            temp_cap += float(order["total"])
            percent = (temp_cap / total_cap) * 100
            percent = float(int(percent * 100)) / 100
            order["percent"] = percent
            new_orders.append(order)
        else:
            order["percent"] = 100.0
            new_orders.append(order)

    for order in new_orders:
        price = int(float(order["price"]) * 10 ** 8)
        amount = int(float(order["amount"]))
        # TODO: add days/hours ago column
        if order["date"] == "0":
            date_as_int = 0
            admin = True
        else:
            # TODO: trim is not needed
            date_as_int = float("{}.{}".format(order["date"][:10],
                                               order["date"][
                                               10:]))  # Trim millis
            admin = False

        python_date = datetime.datetime.fromtimestamp(date_as_int)

        formatted_orders.append({
            "price": price,
            "orderId": order["orderId"],
            "amount": amount,
            "date": python_date,
            "label": order["label"],
            "total": order["total"],
            "admin": admin,
            "percent": order["percent"]
        })

    formatted_orders = sorted(formatted_orders,
                              key=lambda order: float(order["price"]),
                              reverse=True)

    return formatted_orders


def get_public_orders():
    """"""
    URL = "https://www.occe.io/api/v2/public/orders/ltv_btc"
    try:
        resp = urlopen(URL)
        if resp.code == 200:
            json_obj = json.loads(resp.read())
            if json_obj["result"] == "success":
                buy_orders = json_obj["buyOrders"]
                sell_orders = json_obj["sellOrders"]

                return sell_orders, buy_orders
        else:
            LOGGER.info(resp.status_code)
        # TODO: make refactoring
    except error.HTTPError as err:
        LOGGER.info(err)
    return None
