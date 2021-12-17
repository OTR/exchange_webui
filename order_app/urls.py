"""

"""
from django.urls import path, include

from order_app import views


app_name = "order_app"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("orders/", views.OrderView.as_view(), name="orders"),
    path("bid-ask/", views.BidAskView.as_view(), name="bid-ask"),
    path("take-snapshot/", views.take_snapshot, name="take-snapshot"),

]
