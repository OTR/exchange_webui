"""
Groups are not used so unregister them.
"""
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import OrderSnapshot


admin.site.register(OrderSnapshot)
admin.site.unregister(Group)
