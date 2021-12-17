"""
WSGI config for exchange_webui project.
"""
import os

from django.core.wsgi import get_wsgi_application


os.environ.get('DJANGO_SETTINGS_MODULE', 'config.settings.test_settings')
application = get_wsgi_application()
