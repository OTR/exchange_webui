"""

"""
from django.http import HttpResponse

from services.take_active_orders_snapshot import take_active_orders_snapshot


def take_snapshot_view(request):
    """An end point to make Django run business logic from services."""
    take_active_orders_snapshot()

    return HttpResponse("Good")  # TODO: Remove it
