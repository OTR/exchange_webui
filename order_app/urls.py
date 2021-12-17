"""

"""
from django.urls import path

from .views import BidAskView, take_snapshot_view, orders_view
from .views import SnapshotView, SnapshotDetailView, TaskView, IndexView
from .views import FaucetView, OrderBookEventView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("bid-ask/", BidAskView.as_view(), name="bid-ask"),
    path("faucet/", FaucetView.as_view(), name="faucet"),
    path("events/", OrderBookEventView.as_view(), name="events"),
    path("orders/", orders_view, name="orders"),
    path("take-snapshot/", take_snapshot_view, name="take-snapshot"),
    path("tasks/", TaskView.as_view(), name="tasks"),
    path("snapshots/", SnapshotView.as_view(), name="snapshots"),
    path(
        "snapshots/<int:pk>/",
        SnapshotDetailView.as_view(),
        name="snapshot-detail"
    ),
]
