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
        return "\n".join(
            [row.__str__() for row in self.buy_orders.order_by("-price")]
        )

    def get_sell_orders_as_str(self) -> str:
        """"""
        return "\n".join(
            [row.__str__() for row in self.sell_orders.order_by("-price")]
        )

    def get_order_book_state_change(self) -> list[str]:
        """"""
        previous_row = OrderBookState.objects.filter(id__lt=self.id).last()
        msgs = []

        if previous_row:
            # self.sell_orders.remove(*list(second.sell_orders.all()))
            # curr_orders = self.sell_orders.all()
            # prev_orders = previous_row.sell_orders.all()
            sell_got = SellOrder.objects.filter(
                orderbookstate__in=(self,)).exclude(orderbookstate__in=(previous_row,))
            sell_lost = SellOrder.objects.filter(
                orderbookstate__in=(previous_row,)).exclude(orderbookstate__in=(self,))
            buy_got = BuyOrder.objects.filter(
                orderbookstate__in=(self,)).exclude(orderbookstate__in=(previous_row,))
            buy_lost = BuyOrder.objects.filter(
                orderbookstate__in=(previous_row,)).exclude(orderbookstate__in=(self,))

            local_time = timezone.localtime(self.lookup_time).strftime(
                '%d.%m.%Y %H:%M:%S'
            )
            # I'm {self.id} and trying to compare to {previous_row.id}
            msgs.append(f"{local_time}")
            # 0 - price; 1 - amount; 2 - date
            if buy_lost:
                for bl in buy_lost:
                    if bl.date == self.start_epoch:
                        admin = "(Админский)"
                    else:
                        admin = ""

                    msgs.append(
                        f"Снят оредер на покупку {bl.amount} по цене {bl.price} {admin}")
            if buy_got:
                for bg in buy_got:
                    if bg.date == self.start_epoch:
                        admin = "(Админский)"
                    else:
                        admin = ""

                    msgs.append(
                        f"Появился оредер на покупку {bg.amount} по цене {bg.price} {admin}")
            if sell_lost:
                for sl in sell_lost:
                    if sl.date == self.start_epoch:
                        admin = "(Админский)"
                    else:
                        admin = ""

                    msgs.append(
                        f"Снят оредер на продажу {sl.amount} по цене {sl.price} {admin}")
            if sell_got:
                for sg in sell_got:
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
