"""

"""
from django.views.generic import ListView

from ..models import FaucetAddress


ADDRESS = "LeXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


class FaucetView(ListView):
    """
    Not implemented yet.

    A view to display our own faucet placed on the site.

    `address` - a wallet address of a person who has earned coins.
    """
    model = FaucetAddress
    template_name = "order_app/faucet.html"

    def get_context_data(self, **kwargs) -> dict:
        """Just a stub function to be modified later."""
        context = super().get_context_data(**kwargs)
        context["address"] = ADDRESS  # TODO: for test purpose. Remove it.
        return context
