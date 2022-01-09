"""

"""
import json
import logging
from abc import ABC
from datetime import datetime
from functools import wraps
from hashlib import md5
from typing import Callable
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import urlopen, build_opener, OpenerDirector

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
USE_PROXY = False


def _build_opener(headers: list) -> OpenerDirector:
    """A wrapper around `build_opener` to customize it with headers."""
    opener = build_opener()
    opener.addheaders = headers
    return opener


def wrap_http_proxy(url: str) -> str:
    """
    A basic HTTP proxy to avoid pythonanywhere.com restrictions on access to
    external hosts.

    :param url: origin URL
    :return: wrapped URL
    """
    quoted_url = quote(url)
    code_pattern = "urllib2.urlopen('{}'%2C%20timeout%3D20).read()"
    f_code = code_pattern.format(quoted_url)
    url = "http://tumbolia-two.appspot.com/py/{}".format(f_code)

    return url


def catch_http_error(func: Callable) -> Callable:
    """A decorator to catch HTTPError exceptions."""

    @wraps(func)
    def inner(*args):
        try:
            func_return = func(*args)
        except HTTPError as err:
            if err.code == 502:  # HTTP Error 502: Bad Gateway
                # and USE_PROXY is True
                LOGGER.debug(err.args)
                # TODO: Make another attempt
                raise err
        except Exception as err:
            LOGGER.info(type(err))
            LOGGER.info(err.args)
            raise err
        else:
            return func_return

    return inner


@catch_http_error
def fetch(url: str) -> bytes:
    """"""
    resp = urlopen(url)  # IO
    if resp.code == 200:
        data = resp.read()
        return data
    else:
        LOGGER.info(f"Response code is {resp.code}")
        raise UserWarning("Response code is not 200.")


def fetch_through_proxy(url: str) -> bytes:
    """"""
    final_url = wrap_http_proxy(url)
    data = fetch(final_url)
    return data


class PublicAPIOpener(ABC):
    """"""

    def __init__(self):
        """"""
        self.opener = None


class OCCEPublicAPIOpener(PublicAPIOpener):
    """"""

    def __init__(self):
        """"""
        super(OCCEPublicAPIOpener, self).__init__()
        if USE_PROXY:
            self.fetch = fetch_through_proxy
        else:
            self.fetch = fetch


def validate_order_book(raw_json: bytes) -> dict:
    """TODO: split into smaller functions."""
    try:
        json_obj = json.loads(raw_json)
        if json_obj['result'] == "success":
            sorted_lst = []
            orders = json_obj["data"]["buyOrders"] + json_obj["data"][
                "sellOrders"]
            for order in orders:
                try:
                    date = order["date"]
                except KeyError as err:
                    price = order["price"]
                    LOGGER.info(f"Found admin order at {price}")
                    date = 0
                    admin = True
                finally:
                    row_tuple = (
                        order["price"], order["amount"], order["total"],
                        date, order["type"]
                    )
                sorted_lst.append(row_tuple)
            sorted_lst.sort(key=lambda x: x[0])
            sorted_tuple = tuple(sorted_lst)
            b_hash_tuple = md5(json.dumps(sorted_tuple).encode("UTF-8"))

            return {"_hash": b_hash_tuple.hexdigest(), "data": raw_json}
        else:
            log_msg = "JSON response is not succeed"
            LOGGER.info(log_msg)
            raise UserWarning(log_msg)

    except Exception as err:
        logging.exception(err)
        raise err


def format_orders(orders: dict, is_buy_order: bool = False) -> list:
    """Take orders class json object"""
    formatted_orders = []
    new_orders = []
    orders = sorted(orders,
                    key=lambda _order: float(_order["price"]),
                    reverse=is_buy_order
                    )
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
        # FIXME: Define numerical representation for each pair in config
        #  not here
        # price = int(float(order["price"]) * 10 ** 8)
        price = float(order["price"])
        amount = int(float(order["amount"]))
        # TODO: add days/hours ago column
        # { block hack }
        # for some orders server doesn't return `date` in JSON
        if "date" not in order:
            order["date"] = 0
        # { endblock hack }
        if order["date"] == 0:
            date_as_int = 0
            admin = True
        else:
            # Trim millis to prevent `OSError [Errno 22] Invalid argument`
            date_as_int = order["date"] // 1000
            admin = False

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

    formatted_orders = sorted(
        formatted_orders,
        key=lambda _order: float(_order["price"]),
        reverse=True
    )

    return formatted_orders
