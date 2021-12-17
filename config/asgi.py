"""
ASGI config for exchange_webui project.
"""
import os

from django.core.asgi import get_asgi_application


os.environ.get('DJANGO_SETTINGS_MODULE', 'config.settings.test_settings')
application = get_asgi_application()
