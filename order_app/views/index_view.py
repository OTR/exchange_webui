"""

"""
import logging

from django.views.generic import TemplateView


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class IndexView(TemplateView):
    """A view to display root page of the site."""
    template_name = "order_app/base.html"

    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)

        return context
