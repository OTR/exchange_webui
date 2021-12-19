"""

"""
import json
import logging
from datetime import datetime
from hashlib import md5
from urllib.parse import quote
from urllib.request import urlopen

from django.conf import settings


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def fetch(url):
    """"""
    if settings.ALLOWED_HOSTS:
        if settings.ALLOWED_HOSTS[0].endswith(".pythonanywhere.com"):
            # Use proxy
            quoted_addr = quote(url)
            code_pattern = "urllib2.urlopen('{}'%2C%20timeout%3D20).read()"
            f_code = code_pattern.format(quoted_addr)
            url = "http://tumbolia-two.appspot.com/py/{}".format(f_code)
        else:
            pass  # Django is running from localhost
    else:
        logger.debug("settings.ALLOWED_HOSTS is not defined")
        return None
    try:
        resp = urlopen(url)
        if resp.code == 200:
            data = resp.read()
            return data
        else:
            logger.info(f"Response code is {resp.code}")
            return None
    except Exception as exception:
        # logger.exception()
        logger.info(type(exception))
        logger.info(exception.args)
        raise exception


def validate_order_book(data):
    """"""
    try:
        json_obj = json.loads(data)
        if json_obj['result'] == "success":
            sorted_lst = []
            orders = json_obj["data"]["buyOrders"] + json_obj["data"]["sellOrders"]
            for order in orders:
                row_tuple = (
                    order["price"], order["amount"], order["total"],
                    order["date"], order["orderId"], order["label"],
                    order["type"]
                )
                sorted_lst.append(row_tuple)
            sorted_lst.sort(key=lambda x: x[0])
            sorted_tuple = tuple(sorted_lst)
            b_hash_tuple = md5(json.dumps(sorted_tuple).encode("UTF-8"))

            return {"_hash": b_hash_tuple.hexdigest(), "data": data}
        else:
            logger.info("JSON response is not succeed")
            return None

    except Exception as err:
        logging.exception(err)
        raise err


def format_orders(orders, is_buy_order=False):
    """Take orders class json object"""
    formatted_orders = []
    new_orders = []
    orders = sorted(orders,
                    key=lambda _order: float(_order["price"]),
                    reverse=is_buy_order
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
        # block hack
        try:
            date = order["date"]
        except KeyError as err:
            pass
        finally:
            order["date"] = 0
        # endblock hack
        if order["date"] == 0:
            date_as_int = 0
            admin = True
        else:
            # Trim millis to prevent `OSError [Errno 22] Invalid argument`
            date_as_int = order["date"] // 100
            admin = False

        # FIXME: BUG says 2488 but should be 2021
        python_date = datetime.fromtimestamp(date_as_int)

        formatted_orders.append({
            "price": price,
            # "orderId": order["data"]["orderId"],
            "amount": amount,
            "date": python_date,
            # "label": order["label"],
            "total": order["total"],
            "admin": admin,
            "percent": order["percent"]
        })

    formatted_orders = sorted(formatted_orders,
                              key=lambda _order: float(_order["price"]),
                              reverse=True)

    return formatted_orders


"""
data == b"HTTPError: HTTP Error 502: Bad Gateway\n"
"""
