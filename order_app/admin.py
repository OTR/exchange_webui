"""

"""
from django.contrib import admin
from django.contrib.auth.models import Group

from order_app.models import (
    ActiveOrdersRawJSON, SellOrder, BuyOrder, OrderBookState
)


class OrderSnapshotAdmin(admin.ModelAdmin):
    """"""
    readonly_fields = ("lookup_time", "hash_as_hex", "data_as_string")
    fields = ("lookup_time", "hash_as_hex", "data_as_string")


class OrderAdmin(admin.ModelAdmin):
    """"""
    # readonly_fields = ("lookup_time", "hash_as_hex", "data_as_string")
    # fields = ("lookup_time", "hash_as_hex", "data_as_string")
    list_display = ("price", "amount", "total", "date", "order_id", "label")
    list_filter = ("date",)
    date_hierarchy = "date"
    readonly_fields = ("price", "amount", "total", "date", "order_id", "label")
    fields = ("price", "amount", "total", "date", "order_id", "label")

    def get_ordering(self, request):
        """"""
        return ["price"]


class SellOrderInline(admin.TabularInline):
    """"""
    model = OrderBookState.sell_orders.through


class OrderBookStateAdmin(admin.ModelAdmin):
    """"""
    # inlines = (SellOrderInline,)
    # readonly_fields = ("lookup_time", "buy_orders", "sell_orders")
    fields = ("lookup_time", "sell_orders", "buy_orders")


admin.site.unregister(Group)
admin.site.register(ActiveOrdersRawJSON, OrderSnapshotAdmin)
admin.site.register(BuyOrder, OrderAdmin)
admin.site.register(SellOrder, OrderAdmin)
admin.site.register(OrderBookState, OrderBookStateAdmin)
