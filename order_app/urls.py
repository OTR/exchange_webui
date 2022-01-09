"""
End points description:

`index` - TODO: Not implemented yet. Root page of the site, show description
            of the app and some help message.
`active-orders` -
`bid-ask` -
`events` -
`take-snapshot` - a dirty hack to make Django request foreign API, synchronously
                block the program, TODO: use Celery instead.
`snapshots` - show a list of collected snapshots (a bunch of raw json responses
              when getting request to `get active orders by trade pair` API end
              point)
`snapshot-detail` - detailed view of a certain snapshot, literally shows RAW
                    json response taken at the time of observation.
"""
from django.urls import path

import order_app.apps
from order_app.views import (
    ActiveOrderView, BidAskView, IndexView, OrderBookEventView,
    SnapshotDetailView, ActiveOrdersRawJSONView, take_snapshot_view
)


app_name = order_app.apps.OrderAppConfig.name
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("active-orders/", ActiveOrderView.as_view(), name="active-orders"),
    path("bid-ask/", BidAskView.as_view(), name="bid-ask"),
    path("events/", OrderBookEventView.as_view(), name="events"),
    path("take-snapshot/", take_snapshot_view, name="take-snapshot"),
    path("snapshots/", ActiveOrdersRawJSONView.as_view(), name="snapshots"),
    path(
        "snapshots/<int:pk>/",
        SnapshotDetailView.as_view(),
        name="snapshot-detail"
    ),
]


