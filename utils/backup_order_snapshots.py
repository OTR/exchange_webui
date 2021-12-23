"""

"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test_settings")
import django

django.setup()
from order_app.models import OrderSnapshot


class Row(object):
    """"""
    rows = []

    def __init__(self, index, db_row):
        """"""
        self.number = index
        self.id = db_row.id
        self.lookup_time = db_row.lookup_time
        self.hash_ = db_row.hash_
        self.data = db_row.data

        self.rows.append(self)

    def backup(self):
        """"""
        with open(f"{self.lookup_time.timestamp()}.json", "wb") as f1:
            f1.write(self.data)


if __name__ == "__main__":
    for index, db_row in enumerate(OrderSnapshot.objects.order_by("id")):
        Row(index, db_row)

    for row in Row.rows:
        row.backup()
