### Description

### Installation

Via Pip

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
### Setting up environment variables

`$ export DJANGO_SETTINGS_MODULE=config.settings.prod_settings`

(Windows)

Control Panel > User Accounts > Change environment variables

### TODO List

rename `bootstrap.css` to `bootstrap-4.4.1.css`
