"""

"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test_settings")
import django

django.setup()
from order_app.models import ActiveOrdersRawJSON


class Row(object):
    """"""
    rows = []

    def __init__(self, index, db_row):
        """"""
        self.number = index
        self.id = db_row.id
        self.lookup_time = db_row.lookup_time
        self.hash_field = db_row.hash_field
        self.raw_json = db_row.raw_json

        self.rows.append(self)

    def backup(self) -> None:
        """"""
        with open(f"{self.lookup_time.timestamp()}.json", "wb") as f1:
            f1.write(self.raw_json)


if __name__ == "__main__":
    for index, db_row in enumerate(ActiveOrdersRawJSON.objects.order_by("id")):
        Row(index, db_row)

    for row in Row.rows:
        row.backup()
