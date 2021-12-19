"""

"""
import logging

from django.views.generic import TemplateView


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class IndexView(TemplateView):
    """"""
    template_name = "order_app/base.html"

    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        # do something
        # logger.info("From index view")
        return context
