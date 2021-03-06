"""

"""
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """A view to display root page of the site."""
    template_name = "order_app/base.html"

    def get_context_data(self, **kwargs) -> dict:
        """Just a stub function to be modified later."""
        context = super().get_context_data(**kwargs)

        return context
