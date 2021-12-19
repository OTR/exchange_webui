"""
Concrete settings for local test environment.
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

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'  # FIXME: not used
STATIC_DIR = BASE_DIR / "static"
STATICFILES_DIRS = [STATIC_DIR]
STATIC_URL = '/static/'
TIME_ZONE = 'Etc/GMT-3'
