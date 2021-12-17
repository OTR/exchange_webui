"""

"""
from django.views.generic import ListView

from ..models.task import Task


class TaskView(ListView):
    """
    Not Implemented yet.
    A view to display backend tasks of a certain user,
    they desire to complete them automatically.
    """
    model = Task
    template_name = "order_app/tasks.html"
