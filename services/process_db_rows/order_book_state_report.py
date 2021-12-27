"""
Classes used to produce verbose text report about open or closed orders between
two observations (nearest OrderBookState records).
"""
from datetime import datetime
from typing import NamedTuple

from django.conf import settings
from django.db.models import DateTimeField
from django.utils import timezone


DATE_FORMAT = settings.U_DATE_FORMAT
ADMIN_ORDER = settings.U_ADMIN_ORDER
VERBOSE_REPORT_PATTERNS = settings.U_VERBOSE_REPORT_PATTERS


class ReportMaker(object):
    """"""

    def __init__(
            self,
            lookup_time: DateTimeField,
            orders_to_combine: NamedTuple
    ) -> None:
        """Instance variables for combining a report."""
        self.lookup_time = lookup_time
        self.orders_to_combine = orders_to_combine
        self.order_handler = None

    def set_orders_handler(self, concrete_handler) -> None:
        """
        Instantiate concrete handler that will be used in combining
        verbose report depending on exchange we make API calls to
        """
        self.order_handler = concrete_handler()

    def combine_report(self) -> str:
        """"""
        report_message = []
        local_time = timezone.localtime(self.lookup_time).strftime(DATE_FORMAT)
        report_message.append(local_time)

        for field in getattr(self.orders_to_combine, "_fields"):
            for order in getattr(self.orders_to_combine, field):
                report_message.append(
                    self.order_handler.handle_order_fields(order)
                )

        report_message.append("_" * 80)

        return "\n".join(report_message)


class OCCEReportHandler(object):
    """
    A concrete class used to generate different reports depending on
    exchange we use.

    `start_epoch` is a class attribute used to reference to
     UNIX start epoch time.
    """
    start_epoch = datetime.utcfromtimestamp(0)

    @staticmethod
    def handle_order_fields(order, order_type: str) -> str:
        """
        An order with date field set to 0 looks suspicious because usually
        that field set to date the order was made on so mark them as admin
        orders
        """
        if order.date == OCCEReportHandler.start_epoch:
            is_admin = ADMIN_ORDER
        else:
            is_admin = ""

        return VERBOSE_REPORT_PATTERNS[order_type].format(
            order_name=order.name,
            order_amount=order.amount,
            admin=is_admin
        )
