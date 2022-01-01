"""
Exchange_wui URL configuration.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("order_app.urls", namespace="order_app")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
