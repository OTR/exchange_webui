"""

"""
import json
from pprint import pformat

from django.views.generic import DetailView

from ..models.order_snapshot import OrderSnapshot


class SnapshotDetailView(DetailView):
    """
    A view to display details about a certain snapshot (a state of the order
    book at the moment of observation).
    """
    model = OrderSnapshot
    template_name = "order_app/snapshot_detail.html"

    def get_context_data(self, **kwargs) -> dict:
        """
        TODO: field lookup and formatting should be moved into
         `get_pretty_dict` model method, which is not implemented yet.

         Display JSON response as text.
        """
        context = super().get_context_data(**kwargs)
        pretty_dict = pformat(json.loads(context["object"].data))
        context["object"].pretty = pretty_dict

        return context
