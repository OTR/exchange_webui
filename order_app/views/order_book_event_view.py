"""

"""
from django.views.generic import ListView

from ..models import OrderBookState


class OrderBookEventView(ListView):
    """
    A view to get a detailed report about changes of Order Book state, e.g.,

    [12.04.2021][14:50:00] A sell order of 4 coins at 0.04 price has placed in
        the order book
    [12.04.2021][16:34:00] A buy order of 3 coins at 0.03 price has removed
        from the order book
    """
    model = OrderBookState
    template_name = "order_app/events.html"
