"""
https://github.com/iiw/Crex24.Examples/blob/master/python/app.py
https://github.com/ccxt/ccxt/wiki/Manual
"""
import json
from datetime import datetime
from hashlib import md5
from urllib.request import urlopen


def recent_trades(pair):
    """
    Example:

    {
        "price": 0.0158989,
        "volume": 0.242679,
        "side": "buy",
        "timestamp": "2018-05-31T10:08:45Z"
    }
    """
    url = f"https://api.crex24.com/v2/public/recentTrades?instrument={pair}"
    json_obj = json.loads(urlopen(url).read())
    time_as_str = json_obj[0]["timestamp"]
    time = datetime.strptime(time_as_str, "%Y-%m-%dT%H:%M:%SZ")


def order_book(pair):
    """
    JSON Example:

    {
        "buyLevels": [
            {
                "price": 0.01573481,
                "volume": 0.032
            },
            {
                "price": 0.01500001,
                "volume": 0.75
            },
        ]
    }
    """
    url = f"https://api.crex24.com/v2/public/orderBook?instrument={pair}"
    json_obj = json.loads(urlopen(url).read())
    buy_orders = json_obj["buyLevels"]
    sell_orders = json_obj["sellLevels"]


def ltv_ticker(pair):
    """"""
    lst = md5()
    sorted_lst = [0, 0, 0, 0, 0, 0, 0]
    url = f"https://www.occe.io/api/v2/public/info/{pair}"
    try:
        resp = urlopen(url)
        if resp.code == 200:
            raw_data = resp.read()
            json_obj = json.loads(raw_data)
            if json_obj is not None:
                if json_obj["result"] == "success":
                    info = json_obj["coinInfo"][0]

                    sorted_lst[0] = info["lastPrice"]
                    sorted_lst[1] = info["volume24h"]
                    sorted_lst[2] = info["highest24h"]
                    sorted_lst[3] = info["lowest24h"]
                    sorted_lst[4] = info["change24h"]
                    sorted_lst[5] = info["highestBuy"]
                    sorted_lst[6] = info["lowestSell"]

                    sorted_tuple = tuple(sorted_lst)

                    formatted_time = datetime.now().strftime(
                        '%d.%m.%Y %H:%M:%S')
                    _hash = md5(json.dumps(sorted_lst).encode("UTF-8"))
                    if lst != _hash:
                        print(f"{formatted_time} {_hash.hexdigest()}")
                else:
                    pass  # logger.info
            else:
                pass  # logger.info
        else:
            pass  # logger.info
    except Exception as err:
        pass  # logger.info
        raise err


if __name__ == "__main__":
    # PAIR = "DOGE-BTC"
    # recent_trades(PAIR)
    # order_book(PAIR)

    ltv_ticker("ltv_btc")
