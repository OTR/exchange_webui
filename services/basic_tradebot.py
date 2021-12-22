"""

"""
import hashlib
import hmac
from importlib import import_module
from urllib.request import urlopen

import requests

import config

PRIV_KEY = config.PRIV_KEY
PUB_KEY = config.PUB_KEY
PUBLIC_API_CONF = import_module(f"{settings._USE_EXCHANGE}.public_api")

class TradeBot(object):
    """"""
    time_url = "https://www.occe.io/api/v1/tradeview/time"
    user_info_url = "https://www.occe.io/api/v2/user/info"

    def __init__(self, priv_key, pub_key):
        """"""
        self.priv_key = priv_key
        self.pub_key = pub_key

    def _combine_msg(self, HTTP_verb, URI, timestamp, optional_params):
        """"""
        access_key = self.pub_key

        params = {"access_key": access_key,
                  "timestamp": timestamp}

        if optional_params is not None:
            pass  # params.update()

        verbose_params = "&".join(
            ("{}={}".format(key, value) for (key, value) in params.items())
        )

        msg = "{HTTP_verb}|{URI}|{verbose_params}".format(
            HTTP_verb=HTTP_verb,
            URI=URI,
            verbose_params=verbose_params)

        return msg

    def _get_signature(self, msg):
        """"""
        secret_key = self.priv_key

        signature = hmac.new(bytes(secret_key, "latin-1"),
                             msg=bytes(msg, "latin-1"),
                             digestmod=hashlib.sha256).hexdigest()  # .upper()

        return signature

    # def create_sha256_signature(self, msg):
    #     byte_key = binascii.unhexlify(self.PRIVKEY)
    #     msg = msg.encode()
    #     return hmac.new(byte_key, msg, hashlib.sha256).hexdigest().upper()

    # def pycryptodome_signature(self, msg):

    # 	secret_key = self.PRIVKEY

    # 	h = HMAC.new(secret_key.encode(), digestmod=SHA256)
    # 	h.update(msg.encode())
    # 	signature = h.hexdigest()#.upper()
    # 	return signature

    def _get_timestamp(self):
        """"""
        resp = urlopen(self.time_url)
        if resp.status_code == 200:
            return resp.read()
        else:
            raise UserWarning("Response code is not 200")

    def get_user_info(self):
        """"""
        http_method = "GET"
        uri = "/api/v2/user/info"
        access_key = self.pub_key
        timestamp = self._get_timestamp()

        msg = self._combine_msg(http_method, uri, timestamp,
                                optional_params=None)
        signature = self._get_signature(msg)
        # signature = self.create_sha256_signature(msg)
        # signature = self.pycryptodome_signature(msg)
        resp = urlopen(self.user_info_url,
                       params={"access_key": access_key,
                               "signature": signature,
                               "timestamp": timestamp,
                               }
                       )

        if resp.status_code == 200:
            print("OK")
            print(resp.read())
            print(resp.json())
        elif resp.status_code == 401:
            print(resp.read())
            print(resp.PUBLIC_INFO_LTV_BTC)
        else:
            raise UserWarning("Unknown status code")

    def get_my_open_orders(self):
        """"""
        URL = "https://www.occe.io/api/v2/user/orders/open/ltv_btc"
        HTTP_verb = "GET"
        URI = "/api/v2/user/orders/open/ltv_btc"
        access_key = self.pub_key
        timestamp = self._get_timestamp()

        msg = self._combine_msg(HTTP_verb, URI, timestamp, optional_params=None)
        print(msg)
        signature = self._get_signature(msg)
        print(signature)
        resp = requests.get(URL, params={"access_key": access_key,
                                         "signature": signature,
                                         "timestamp": timestamp,
                                         })
        print(resp.status_code)
        print(resp.json())

    def get_open_orders(self):
        """"""
        URL = "https://www.occe.io/api/v2/public/orders/ltv_btc"
        resp = requests.get(URL)
        # if resp.status_code == 200:
        json_obj = resp.json()
        # if json_obj["result"] == "success"
        buy_orders = json_obj["buyOrders"]
        sell_orders = json_obj["sellOrders"]
        print(buy_orders)


if __name__ == "__main__":
    LTVBot = TradeBot(
        priv_key=PRIV_KEY,
        pub_key=PUB_KEY)
    # LTVBot.get_user_info()
    LTVBot.get_open_orders()
