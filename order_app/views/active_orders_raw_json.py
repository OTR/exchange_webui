"""

"""
from django.views.generic import ListView

from order_app.models import ActiveOrdersRawJSON


class ActiveOrdersRawJSONView(ListView):
    """Not Implemented yet."""
    model = ActiveOrdersRawJSON
    paginate_by = 10
    template_name = "order_app/snapshots.html"
