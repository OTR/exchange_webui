"""
Concrete production settings for `pythonanywhere.com`

Variables with leading underscore mean user defined settings, not Django's
"""
import os

from .prod_settings import *


# Your login on hosting
U_LOGIN = os.environ.get("LOGIN")
U_DB_PASSWD = os.environ.get("DB_PASSWD")
# MySQL table name, creates on a dashboard
U_TABLE_NAME = "order_app"

ALLOWED_HOSTS = [f"{U_LOGIN}.pythonanywhere.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": f"{U_LOGIN}${U_TABLE_NAME}",
        "HOST": f"{U_LOGIN}.mysql.pythonanywhere-services.com",
        "USER": f"{U_LOGIN}",
        "PASSWORD": f"{U_DB_PASSWD}"
    }
}

TIME_ZONE = "Etc/GMT-3"  # UTC+3
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = f"/home/{U_LOGIN}/config/media"
MEDIA_URL = "/media/"
STATIC_ROOT = f"/home/{U_LOGIN}/config/static"
STATIC_URL = "/static/"
