"""

"""
from django.db import models


class Task(models.Model):
    """
    A model that contains backend tasks for a certain user,
    that desire to complete them automatically.
    """
    title = models.CharField(max_length=255)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        """"""
        return self.title
