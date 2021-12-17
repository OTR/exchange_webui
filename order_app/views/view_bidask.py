"""

"""
import logging

from django.views.generic import TemplateView

# from ..views.fetcher import foo
# from ..models import BestPriceLTV


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BidAskView(TemplateView):
    """TODO: BidAskView(ListView) ???"""
    # model = BestPriceLTV
    # paginate_by = 10
    template_name = "order_app/bid_ask.html"

    # extra_context = {"title": "Whatsoever"}

    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        # context["xos"] = foo()
        return context
