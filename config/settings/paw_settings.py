"""
Concrete production settings for `pythonanywhere.com`
"""
import os

from .prod_settings import *


# Your login on hosting
_LOGIN = os.environ.get("LOGIN")
_DB_PASSWD = os.environ.get("DB_PASSWD")
# MySQL table name, creates on a dashboard
_TABLE_NAME = "order_app"

ALLOWED_HOSTS = [f"{_LOGIN}.pythonanywhere.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': f'{_LOGIN}${_TABLE_NAME}',
        'HOST': f'{_LOGIN}.mysql.pythonanywhere-services.com',
        'USER': f'{_LOGIN}',
        'PASSWORD': f'{_DB_PASSWD}'
    }
}

TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = f'/home/{_LOGIN}/config/media'
MEDIA_URL = '/media/'
STATIC_ROOT = f'/home/{_LOGIN}/config/static'
STATIC_URL = '/static/'
