"""
Concrete settings for local test environment.
"""
import os

from .common_settings import *


ALLOWED_HOSTS = ["127.0.0.1"]
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / ".app_data" / 'db.sqlite3',
    }
}

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'  # FIXME: not used
STATIC_DIR = BASE_DIR / "static"
STATICFILES_DIRS = [STATIC_DIR]
STATIC_URL = '/static/'
TIME_ZONE = 'Etc/GMT-3'

# USER DEFINED SETTINGS (NOT DJANGO's)

# Which exchange API make calls to
_USE_EXCHANGE = "config.exchanges.occe"

# A directory to keep backup files
BACKUP_DIR = BASE_DIR / ".backup"

# User private key to access private API on exchange site
PRIV_KEY = os.environ.get("PRIV_KEY")
PUB_KEY = os.environ.get("PUB_KEY")
