"""
Settings for production use.
"""
from django.core.exceptions import ImproperlyConfigured

from .common_settings import *


def change_it() -> None:
    """
    Run `python -c 'from django.core.management.utils import
    get_random_secret_key; print(get_random_secret_key())'`
    to generate a new secret key.
    """
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")


ALLOWED_HOSTS = []
DEBUG = False
SECRET_KEY = "" or change_it()
