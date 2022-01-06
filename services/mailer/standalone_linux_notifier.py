"""
A standalone script for linux to be running infinitely and checking if fields
 in JSON response has changed, uses a pickle file to keep previous values to
 compare on the next iteration, or compare with if execution of the script
 was interrupted.

Uses linux utility `mail` to send email letters.
Reference: https://www.commandlinux.com/man-page/man1/Mail.1.html

Email body pattern to be filled in and a command to send a letter are defined in
 a config file placed at `./config/email/email_pattern.py` from project root.
"""
import os
from pathlib import Path
from decimal import Decimal
from importlib import import_module
from services.fetcher.fetch import fetch
import json
import pickle
from time import sleep

from config.email.email_pattern import MAIL_BODY, SHELL_COMMAND


# What Django settings to use: `test`, `prod`, etc.
# needed to get exchange settings
DJANGO_SETTINGS_VARIABLE = os.environ.get(
    "DJANGO_SETTINGS_MODULE",
    "config.settings.test_settings"
)
DJANGO_SETTINGS_MODULE = import_module(DJANGO_SETTINGS_VARIABLE)

# Get settings about exchange market to make API calls to
# methods, endpoints, etc
USE_EXCHANGE = DJANGO_SETTINGS_MODULE.U_USE_EXCHANGE
PUBLIC_API_CONF = import_module(f"{USE_EXCHANGE}.public_api")

# a URL to get summary information about trade history by given trade pair
TRADE_HISTORY_BY_PAIR_PATTERN = PUBLIC_API_CONF.TRADE_HISTORY_BY_PAIR_PATTERN
TRADE_PAIR = PUBLIC_API_CONF.TRADE_PAIR

# Receiver email address to send letters with information about price change
EMAIL_RECEIVER = os.environ.get("EMAIL_RECEIVER")
EMAIL_SUBJECT = "{pair} Price Change".format(pair=TRADE_PAIR.replace("_", " "))

BASE_DIR = Path(__file__).parent.parent.parent
PATH_TO_PREV_SERIALIZED_STATE = BASE_DIR / ".app_data" / "prev_state.dat"

# A delay between API calls in seconds
API_CALL_DELAY = 60


class PickleHandler(object):
    """A class to work with serialized data file."""
    def __init__(self, path_to_pickle: Path) -> None:
        """
        `self._current_prices` - a dict with keys "last_price", "highest_buy",
        "lowest_sell"a data about prices which will be saved if
        pickle file doesn't exist or when updating the data.
        TODO: maybe use namedtuple instead?

        :param path_to_pickle: a path where serialized data file is placed.
        """
        self.path: Path = path_to_pickle
        self._current_prices: dict = {}

    @property
    def current_prices(self) -> dict:
        """
        A getter method to set current prices as initial data if pickle file
        doesn't exist.

        :return: a dict with keys "last_price", "highest_buy", "lowest_sell"
        """
        return self._current_prices

    @current_prices.setter
    def current_prices(self, value: dict) -> None:
        """"""
        self._current_prices: dict = value

    def load(self) -> dict:
        """"""
        with open(self.path, "rb") as cm:
            previous_prices = pickle.load(cm)
        return previous_prices

    def dump(self, data_to_dump) -> None:
        """"""
        with open(self.path, "wb") as cm:
            pickle.dump(data_to_dump, cm)

    def load_previous_or_dump_current(self) -> dict:
        """"""
        if os.path.exists(self.path):
            previous_prices: dict = self.load()
            return previous_prices
        else:
            self.dump(data_to_dump=self.current_prices)
            return {}


def load_current_prices_from_json(raw_json: bytes) -> dict:
    """"""
    price_json: dict = json.loads(raw_json)
    coin_info: dict = price_json["data"]["coinInfo"][0]
    last_price: Decimal = Decimal(str(coin_info["lastPrice"]))
    highest_buy: Decimal = Decimal(str(coin_info["highestBuy"]))
    lowest_sell: Decimal = Decimal(str(coin_info["lowestSell"]))

    return {
        "last_price": last_price,
        "highest_buy": highest_buy,
        "lowest_sell": lowest_sell
    }


def combine_email_body(curr_prices: dict, prev_prices: dict) -> str:
    """
    Fill in email body pattern with variables about price change.

    :return combined email body to be sent.
    """
    email_body: str = MAIL_BODY.format(
        trade_pair=TRADE_PAIR,

        curr_last_price=curr_prices["last_price"],
        curr_highest_buy=curr_prices["highest_buy"],
        curr_lowest_sell=curr_prices["lowest_sell"],

        prev_last_price=prev_prices["last_price"],
        prev_highest_buy=prev_prices["highest_buy"],
        prev_lowest_sell=prev_prices["lowest_sell"],
    )

    return email_body


def send_email(with_body, with_subject, to_address) -> None:
    """"""
    os.system(SHELL_COMMAND.format(
       body=with_body, subject=with_subject, mailto=to_address
    ))


def main() -> None:
    """

    """
    api_url: str = TRADE_HISTORY_BY_PAIR_PATTERN.format(pair=TRADE_PAIR)
    json_response: bytes = fetch(api_url)
    curr_prices: dict = load_current_prices_from_json(json_response)
    handler = PickleHandler(path_to_pickle=PATH_TO_PREV_SERIALIZED_STATE)
    handler.current_prices = curr_prices
    prev_prices: dict = handler.load_previous_or_dump_current()
    if prev_prices and not curr_prices == prev_prices:
        email_body: str = combine_email_body(
            curr_prices=curr_prices, prev_prices=prev_prices
        )
        send_email(
            with_body=email_body,
            with_subject=EMAIL_SUBJECT,
            to_address=EMAIL_RECEIVER
        )
        handler.dump(curr_prices)


if __name__ == "__main__":
    # An infinity loop to check for price change with a delay
    while True:
        main()
        sleep(API_CALL_DELAY)
