"""
Concrete settings for local test environment.

Variables with leading "U_" mean user defined settings, not Django's
"""
import os

from .common_settings import *
from services.process_db_rows.order_book_state_report import OCCEReportHandler


ALLOWED_HOSTS = ["127.0.0.1"]
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / ".app_data" / "db.sqlite3",
    }
}

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"  # FIXME: not used
STATIC_DIR = BASE_DIR / "static"
STATICFILES_DIRS = [STATIC_DIR]
STATIC_URL = "/static/"
TIME_ZONE = "Etc/GMT-3"  # UTC+3

# ______________________________________________________________________________
# USER DEFINED SETTINGS, NOT DJANGO ONES (with leading "U_")

# Which exchange API make calls to
U_USE_EXCHANGE = "config.exchanges.occe"

# A directory to keep backup files
U_BACKUP_DIR = BASE_DIR / ".backup"

# User's private and public keys to access private API on exchange site
U_PRIV_KEY = os.environ.get("OCCE_PRIV_KEY")
U_PUB_KEY = os.environ.get("OCCE_PUB_KEY")

# Date format to display as verbose name on Django admin site
# Reference: https://docs.python.org/3/library/time.html#time.strftime
U_DATETIME_FORMAT = "%d.%m.%Y %H:%M:%S"

# A class that defines OrderBookState change report combining
U_REPORT_HANDLER = OCCEReportHandler

# Patterns to produce a verbose report
U_VERBOSE_REPORT_PATTERS = {
    "closed_buy_orders": "Снят оредер на покупку {order_amount} по цене "
                         "{order_price} {admin}",
    "open_buy_orders": "Появился оредер на покупку {order_amount} по цене"
                       "{order_price} {admin}",
    "closed_sell_orders": "Снят оредер на продажу {order_amount} по цене "
                          "{order_price} {admin}",
    "open_sell_orders": "Появился оредер на продажу {order_amount} по цене "
                        "{order_price} {admin}",
}

# Verbose name for a suspicious order
U_ADMIN_ORDER = "(Админский)"
