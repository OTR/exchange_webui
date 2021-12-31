"""

"""
import logging

from django.views.generic import TemplateView


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class BidAskView(TemplateView):
    """TODO: BidAskView(ListView) ???"""
    template_name = "order_app/bid_ask.html"

    def get_context_data(self, **kwargs) -> dict:
        """Just a stub function to be modified later."""
        context = super().get_context_data(**kwargs)

        return context
