"""

"""
from django.db import models
from django.utils import timezone


class OrderSnapshot(models.Model):
    """"""
    time_format = "%d.%m.%Y %H:%M:%S"
    lookup_time = models.DateTimeField("lookup time", default=timezone.now)
    hash_field = models.CharField(max_length=32)
    data = models.BinaryField(max_length=32 * 1024)  # 32 KiB

    def __str__(self):
        """Verbose name of a database record to display in Django admin site."""
        local_time = timezone.localtime(self.lookup_time).strftime(
            self.time_format
        )
        hash_ = self.hash_field

        return f"{local_time} {hash_}"

    def hash_as_hex(self):
        """Return hash_field represented as hex."""
        return self.hash_field

    def data_as_string(self):
        """Return data (JSON response) as string."""
        return self.data.decode("UTF-8")