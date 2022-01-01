"""

"""
from django.urls import path

import order_app.apps
from .views import BidAskView, take_snapshot_view, ActiveOrderView
from .views import SnapshotView, SnapshotDetailView, TaskView, IndexView
from .views import FaucetView, OrderBookEventView


app_name = order_app.apps.OrderAppConfig.name
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("active-orders/", ActiveOrderView.as_view(), name="active-orders"),
    path("bid-ask/", BidAskView.as_view(), name="bid-ask"),
    path("events/", OrderBookEventView.as_view(), name="events"),
    path("faucet/", FaucetView.as_view(), name="faucet"),
    path("take-snapshot/", take_snapshot_view, name="take-snapshot"),
    path("tasks/", TaskView.as_view(), name="tasks"),
    path("snapshots/", SnapshotView.as_view(), name="snapshots"),
    path(
        "snapshots/<int:pk>/",
        SnapshotDetailView.as_view(),
        name="snapshot-detail"
    ),
]


