# Description

...

# Installation

## Via Pip

```commandline
$ python -m venv exch_venv
$ cd exch_venv
(Linux) $ source bin/activate
(Windows) $ Scripts\activate.bat
$ git clone https://github.com/OTR/exchange_webui.git exchange
$ cd exchange
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser // (optional)
$ python manage.py runserver
```

# Setting up environment variables

Application configuration in performed by creating a new settings file in 
`/config/settings/` directory and extending `prod_settings.py`
 (`from .prod_settings import *`)

Then you need to set relative path to your custom settings in OS environment 
variable.

`$ export DJANGO_SETTINGS_MODULE=config.settings.prod_settings`

(Windows)

Control Panel > User Accounts > Change environment variables

## A List of variables needed to be set up

No matter what settings you use, you need to override `SECRET_KEY` setting 
(by adding its assignation to your `<custom_settings>.py` file) which is 
empty string by default that caused Django exception.

Reference: [Django Docs | SECRET_KEY](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/#secret-key)

To generate a new secret key, run the following command in your console:

`python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

### Settings for `pythonanywhere.com`

To distinguish between Django and user defined settings, there is a 
convention to name your variables starting with `U_`.

`U_LOGIN` - your account login on the hosting

#### MySQL settings (used by default)

`U_DB_PASSWD` - the password from your database

`U_TABLE_NAME` - the name of the table used by your Django App



### Settings for local test environment

...

### Settings to for with OCCE exhange

...

# SQLite viewer

Simple database viewer SQLite_bro 0.12.1

```
$ apt-get install python3-tk
$ pip install sqlite_bro
$ pip install --upgrade sqlite_bro

$ sqlite_bro -h
```

# TODO List

* rename `bootstrap.css` to `bootstrap-4.4.1.css`

* get rid of [autoreload] logger

* Rename `OrderSnapshot` model to `RawJsonResponseSomething` to reveal it's 
  essence.
  