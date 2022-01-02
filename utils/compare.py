"""

"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test_settings")
import django

django.setup()
from order_app.models import OrderSnapshot
from django.utils import timezone


def compare(self) -> None:
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


if __name__ == "__main__":
    for row, db_row in enumerate(OrderSnapshot.objects.order_by("id")):
        Row(row, db_row)

    for row in Row.rows:
        row.compare()
