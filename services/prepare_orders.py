"""

"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test_settings")
import django

django.setup()
from order_app.models import OrderSnapshot, SellOrder, BuyOrder, OrderBookState
import json
from datetime import datetime
from django.utils import timezone
from hashlib import md5


class Row(object):
    """"""

    rows = []

    def __init__(self, index, db_row):
        """"""
        self.number = index
        self.id = db_row.id
        self.lookup_time = db_row.lookup_time
        self.hash_ = db_row.hash_
        self.data = db_row.data

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
        self.rows.append(self)

    def compare(self):
        """"""
        if self.number == 0:
            self.buy_got = set()
            self.sell_got = set()
            self.buy_lost = set()
            self.sell_lost = set()
        else:
            prev = self.rows[self.number - 1]
            local_time = timezone.localtime(self.lookup_time).strftime(
                '%d.%m.%Y %H:%M:%S'
            )
            print(f"{local_time}:")
            # print(f" I'm {self.id} and trying to compare to {prev.id}")
            self.buy_got = self.buy_set - prev.buy_set
            self.sell_got = self.sell_set - prev.sell_set
            self.buy_lost = prev.buy_set - self.buy_set
            self.sell_lost = prev.sell_set - self.sell_set
            # 0 - price; 1 - amount; 2 - date
            if self.buy_lost:
                for bl in self.buy_lost:
                    if bl[2] == "0":
                        is_admin = "(Админский)"
                    else:
                        is_admin = ""
                    print(
                        f"Снят оредер на покупку {bl[1]} LTV по цене {bl[0]} "
                        f"{is_admin}"
                    )
            if self.buy_got:
                for bg in self.buy_got:
                    if bg[2] == "0":
                        is_admin = "(Админский)"
                    else:
                        is_admin = ""
                    print(
                        f"Появился оредер на покупку {bg[1]} LTV по цене "
                        f"{bg[0]} {is_admin}"
                    )
            if self.sell_lost:
                for sl in self.sell_lost:
                    if sl[2] == "0":
                        is_admin = "(Админский)"
                    else:
                        is_admin = ""
                    print(
                        f"Снят оредер на продажу {sl[1]} LTV по цене "
                        f"{sl[0]} {is_admin}"
                    )
            if self.sell_got:
                for sg in self.sell_got:
                    if sg[2] == "0":
                        is_admin = "(Админский)"
                    else:
                        is_admin = ""
                    print(
                        f"Появился оредер на продажу {sg[1]} LTV по цене "
                        f"{sg[0]} {is_admin}"
                    )
        print("_" * 80)

    def populate_order_table(self):
        """"""
        state, b_created = OrderBookState.objects.get_or_create(
            lookup_time=self.lookup_time)

        for order_type, order_set in (
                ("sell", self.sell_orders), ("buy", self.buy_orders)
        ):
            for row in order_set:
                date_as_int = float(
                    "{}.{}".format(row["date"][:10], row["date"][10:])
                )
                date = datetime.fromtimestamp(date_as_int)
                if order_type == "sell":
                    _Model = SellOrder
                else:
                    _Model = BuyOrder
                obj, created = _Model.objects.get_or_create(
                    amount=row["amount"],
                    date=date,
                    label=row["label"],
                    order_id=row["orderId"],
                    price=row["price"],
                    total=row["total"])
                if not created:
                    print("Cannot create Order coz already created")
                if order_type == "sell":
                    state.sell_orders.add(obj)
                else:
                    state.buy_orders.add(obj)

    def backup(self):
        """"""
        with open(f"{self.lookup_time.timestamp()}.json", "wb") as f1:
            f1.write(self.data)

    def purge(self):
        """"""
        pass


def load():
    """"""
    # FIXME: Use directory constant from `OCCE_config.py`
    backup_dir = os.path.join(os.getcwd(), "../.backup")
    context = {}
    for path, dirs, files in os.walk(backup_dir):
        for _file in files:
            timestamp = float(".".join(_file.split(".")[:2]))
            lookup_time = datetime.fromtimestamp(timestamp)
            with open(os.path.join(path, _file), "rb") as f1:
                try:
                    data = f1.read()
                    if data == b"HTTPError: HTTP Error 502: Bad Gateway\n":
                        print("Minus 1, 502")
                    elif data == b"":
                        print("Minus 2, 118")
                    else:

                        json_obj = json.loads(data)
                        if json_obj is not None:
                            if json_obj["result"] == "success":

                                sorted_lst = []
                                orders = json_obj["buyOrders"] + \
                                         json_obj["sellOrders"]
                                for order in orders:
                                    row_tuple = (
                                        order["price"], order["amount"],
                                        order["total"], order["date"],
                                        order["orderId"], order["label"],
                                        order["type"])
                                    sorted_lst.append(row_tuple)
                                # print(len(sorted_lst))
                                sorted_lst.sort(key=lambda x: x[0])
                                sorted_tuple = tuple(sorted_lst)
                                b_hash_tuple = md5(
                                    json.dumps(sorted_tuple).encode("UTF-8"))
                                # print(
                                # f"{lookup_time}\t{b_hash_tuple.hexdigest().upper()}")
                                ###

                                obj, created = OrderSnapshot.objects.get_or_create(
                                    hash_field=b_hash_tuple.hexdigest())
                                if not created:
                                    # There is a row with given unique hash
                                    print(
                                        "Cannot create Snapshot coz already "
                                        "created"
                                    )
                                else:
                                    # There is NO row with given unique hash
                                    obj.lookup_time = lookup_time
                                    obj.data = data
                                    obj.save()
                            else:
                                raise UserWarning
                        else:
                            raise UserWarning
                except json.decoder.JSONDecodeError as err:
                    print(data)
                    raise err
                except Exception as err:
                    print(
                        f"{lookup_time}\t{hex_data.upper()}\t"
                        f"{b_hash_tuple.hexdigest().upper()}\t{builtin_hex}"
                    )
                    raise err
            # context[date] = {"data"}
        break


if __name__ == "__main__":
    # load()
    for row, db_row in enumerate(OrderSnapshot.objects.order_by("id")):
        Row(row, db_row)

    for row in Row.rows:
        row.compare()
    # row.populate_order_table()
    # row.backup()
