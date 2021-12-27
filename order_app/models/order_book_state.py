"""

"""
from collections import namedtuple

from django.conf import settings
from django.db import models
from django.utils import timezone

from services.process_db_rows.order_book_state_report import ReportMaker
from ..models import BuyOrder, SellOrder


DATE_FORMAT = settings.U_DATE_FORMAT
REPORT_HANDLER = settings.U_REPORT_HANDLER
open_and_closed_orders = namedtuple("OpenNClosedOrders",
                                    [
                                        "lookup_time",
                                        "open_sell_orders",
                                        "closed_sell_orders",
                                        "open_buy_orders",
                                        "closed_buy_orders"
                                    ]
                                    )


class OrderBookState(models.Model):
    """
    A model to keep state of an order book of hardcoded trade pair at lookup
    time.
    """
    lookup_time = models.DateTimeField("lookup time")
    buy_orders = models.ManyToManyField(BuyOrder)
    sell_orders = models.ManyToManyField(SellOrder)

    def __str__(self) -> str:
        """
        :return: verbose name of local time at observation moment.
        """
        return "{}".format(
            timezone.localtime(self.lookup_time).strftime(DATE_FORMAT)
        )

    def get_buy_orders_as_str(self) -> str:
        """"""
        rows = (row.__str__() for row in self.buy_orders.order_by("-price"))
        return "\n".join(rows)

    def get_sell_orders_as_str(self) -> str:
        """
        Select all the sell orders which were placed in an order book with
        descend ordering by price.

        :return: their string representation as multiline string
        """
        rows = (row.__str__() for row in self.sell_orders.order_by("-price"))
        return "\n".join(rows)

    def get_order_book_state_change(self) -> str:
        """
        Compare entries of the previous row with current ones.

        :return: Combined verbose report
        """
        previous_row = OrderBookState.objects.filter(id__lt=self.id).last()

        if not previous_row:
            # Nothing to combine with so return empty string
            return ""

        # TODO: optimize records selection from DB
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

        changed_orders = open_and_closed_orders(
            lookup_time=self.lookup_time,
            open_sell_orders=open_sell_orders,
            closed_sell_orders=closed_sell_orders,
            open_buy_orders=open_buy_orders,
            closed_buy_orders=closed_buy_orders
        )

        report = ReportMaker(
            lookup_time=self.lookup_time,
            orders_to_combine=changed_orders
        )
        report.set_orders_handler(REPORT_HANDLER)

        return report.combine_report()
