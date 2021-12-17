"""
Settings for test environment.
"""
from .common_settings import *


ALLOWED_HOSTS = ["127.0.0.1"]
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / ".app_data" / 'db.sqlite3',
    }
}