"""
Groups are not used so unregister them.
"""
from django.contrib import admin
from django.contrib.auth.models import Group


admin.site.unregister(Group)
