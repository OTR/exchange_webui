"""

"""
import os
import pathlib
from decimal import Decimal
from importlib import import_module
from services.fetcher.fetch import fetch
import json
from urllib.request import urlopen
import pickle
from time import sleep


DJANGO_SETTINGS_VARIABLE = os.environ.get(
    "DJANGO_SETTINGS_MODULE",
    "config.settings.test_settings"
)
DJANGO_SETTINGS_MODULE = import_module(DJANGO_SETTINGS_VARIABLE)
USE_EXCHANGE = DJANGO_SETTINGS_MODULE.U_USE_EXCHANGE
PUBLIC_API_CONF = import_module(f"{USE_EXCHANGE}.public_api")
TRADE_HISTORY_BY_PAIR_PATTERN = PUBLIC_API_CONF.TRADE_HISTORY_BY_PAIR_PATTERN
TRADE_PAIR = PUBLIC_API_CONF.TRADE_PAIR
EMAIL_RECEIVER = os.environ.get("EMAIL_RECEIVER")
BASE_DIR = pathlib.Path(__file__).parent.parent.parent
PATH_TO_PREV_SERIALIZED_STATE_FILE = BASE_DIR / ".app_data" / "prev_state.dat"


class PickleHandler(object):
    """"""
    def __init__(self, path_to_pickle, current_prices):
        """"""
        self.path = path_to_pickle
        self.current_prices = current_prices

    def get_or_create(self):
        """"""
        if os.path.exists(self.path):
            with open(self.path, "rb") as cm:
                previous_prices = pickle.load(cm)
            return previous_prices
        else:
            with open(self.path, "wb") as cm:
                pickle.dump(self.current_prices, cm)


def get_current_prices(raw_json: bytes) -> dict:
    """"""
    price_json = json.loads(raw_json)
    coin_info = price_json["data"]["coinInfo"][0]
    last_price = Decimal(str(coin_info["lastPrice"]))
    highest_buy = Decimal(str(coin_info["highestBuy"]))
    lowest_sell = Decimal(str(coin_info["lowestSell"]))

    return {
        "last_price": last_price,
        "highest_buy": highest_buy,
        "lowest_sell": lowest_sell
    }


def main() -> None:
    """

    """
    api_url = TRADE_HISTORY_BY_PAIR_PATTERN.format(pair=TRADE_PAIR)
    print(api_url)
    json_response = fetch(api_url)
    prices = get_current_prices(json_response)
    print(prices)
    print(PATH_TO_PREV_SERIALIZED_STATE_FILE)


if __name__ == "__main__":
    main()
