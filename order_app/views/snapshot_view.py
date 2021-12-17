"""

"""

from django.views.generic import ListView

from ..models import OrderSnapshot


class SnapshotView(ListView):
    """Not Implemented yet."""
    model = OrderSnapshot
    paginate_by = 10
    template_name = "order_app/snapshots.html"
