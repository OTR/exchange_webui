"""

"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test_settings")
import django

django.setup()
import json


class ActiveOrdersRecord(object):
    """"""

    active_orders_records = []

    def __init__(self, index, db_row) -> None:
        """"""
        self.number = index
        self.id = db_row.id
        self.lookup_time = db_row.lookup_time
        self.hash_field = db_row.hash_field
        self.data = db_row.raw_json

        json_obj = json.loads(self.data)
        self.buy_orders = json_obj["buyOrders"]
        self.sell_orders = json_obj["sellOrders"]
        # 0 - price; 1 - amount; 2 - date
        buy_set = set()
        sell_set = set()
        for _orders, _set in [(self.buy_orders, buy_set),
                              (self.sell_orders, sell_set)]:
            for order in _orders:
                _set.add((int(order["price"] * 10 ** 8), order["amount"],
                          order["date"]))

        self.buy_set = buy_set
        self.sell_set = sell_set
        self.active_orders_records.append(self)
