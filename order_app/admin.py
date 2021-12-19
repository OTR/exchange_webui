"""
Groups are not used so unregister them.
"""
from django.contrib import admin
from django.contrib.auth.models import Group

from order_app.models.order_snapshot import OrderSnapshot


admin.site.register(OrderSnapshot)
admin.site.unregister(Group)
