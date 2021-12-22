"""

"""
from datetime import datetime

from django.db import models
from django.utils import timezone

from ..models import BuyOrder, SellOrder


class OrderBookState(models.Model):
    """"""
    lookup_time = models.DateTimeField("lookup time")
    buy_orders = models.ManyToManyField(BuyOrder)
    sell_orders = models.ManyToManyField(SellOrder)

    start_epoch = datetime.utcfromtimestamp(0)

    def __str__(self):
        """Verbose name is local time of observation moment."""
        return "{}".format(
            timezone.localtime(self.lookup_time).strftime("%d.%m.%Y %H:%M:%S")
        )

    def get_buy_orders_as_str(self):
        """"""
        rows = (row.__str__() for row in self.buy_orders.order_by("-price"))
        return "\n".join(rows)

    def get_sell_orders_as_str(self) -> str:
        """"""
        rows = (row.__str__() for row in self.sell_orders.order_by("-price"))
        return "\n".join(rows)

    def get_order_book_state_change(self) -> list[str]:
        """"""
        previous_row = OrderBookState.objects.filter(id__lt=self.id).last()
        msgs = []

        if previous_row:
            # self.sell_orders.remove(*list(second.sell_orders.all()))
            # curr_orders = self.sell_orders.all()
            # prev_orders = previous_row.sell_orders.all()
            open_sell_orders = SellOrder.objects.filter(
                orderbookstate__in=(self,)
            ).exclude(orderbookstate__in=(previous_row,))
            closed_sell_orders = SellOrder.objects.filter(
                orderbookstate__in=(previous_row,)
            ).exclude(orderbookstate__in=(self,))
            open_buy_orders = BuyOrder.objects.filter(
                orderbookstate__in=(self,)
            ).exclude(orderbookstate__in=(previous_row,))
            closed_buy_orders = BuyOrder.objects.filter(
                orderbookstate__in=(previous_row,)
            ).exclude(orderbookstate__in=(self,))

            local_time = timezone.localtime(self.lookup_time).strftime(
                '%d.%m.%Y %H:%M:%S'
            )
            msgs.append(f"{local_time}")
            # 0 - price; 1 - amount; 2 - date
            if closed_buy_orders:
                for bl in closed_buy_orders:
                    if bl.date == self.start_epoch:
                        admin = "(Админский)"
                    else:
                        admin = ""

                    msgs.append(
                        f"Снят оредер на покупку {bl.amount} по цене {bl.price} {admin}")
            if open_buy_orders:
                for bg in open_buy_orders:
                    if bg.date == self.start_epoch:
                        admin = "(Админский)"
                    else:
                        admin = ""

                    msgs.append(
                        f"Появился оредер на покупку {bg.amount} по цене {bg.price} {admin}")
            if closed_sell_orders:
                for sl in closed_sell_orders:
                    if sl.date == self.start_epoch:
                        admin = "(Админский)"
                    else:
                        admin = ""

                    msgs.append(
                        f"Снят оредер на продажу {sl.amount} по цене {sl.price} {admin}")
            if open_sell_orders:
                for sg in open_sell_orders:
                    if sg.date == self.start_epoch:
                        admin = "(Админский)"
                    else:
                        admin = ""

                    msgs.append(
                        f"Появился оредер на продажу {sg.amount} по цене {sg.price} {admin}")
        else:
            pass  # There is no previous OrderBookState

        msgs.append("_" * 80)
        return "\n".join(msgs)
