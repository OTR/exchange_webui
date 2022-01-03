"""

"""
from django.urls import path

import order_app.apps
from .views import (
    ActiveOrderView, BidAskView, IndexView, OrderBookEventView,
    SnapshotDetailView, SnapshotView, take_snapshot_view
)


app_name = order_app.apps.OrderAppConfig.name
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("active-orders/", ActiveOrderView.as_view(), name="active-orders"),
    path("bid-ask/", BidAskView.as_view(), name="bid-ask"),
    path("events/", OrderBookEventView.as_view(), name="events"),
    path("take-snapshot/", take_snapshot_view, name="take-snapshot"),
    path("snapshots/", SnapshotView.as_view(), name="snapshots"),
    path(
        "snapshots/<int:pk>/",
        SnapshotDetailView.as_view(),
        name="snapshot-detail"
    ),
]


