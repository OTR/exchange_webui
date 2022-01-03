"""

"""
from random import randint, seed
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import BestPrice


class BestPriceModelTest(TestCase):
    """"""

    def setUp(self) -> None:
        """Fill in test database's table."""
        price_range = (300.0, 900.0)  # Spread for test set
        # Get arithmetic mean value
        mean = int((price_range[1] - price_range[0]) / 2)
        for i in range(40):
            best_sell = randint(mean, price_range[1])  # From middle to high
            seed()
            best_buy = randint(price_range[0], mean)  # From low to middle
            seed()
            BestPrice.objects.create(
                best_sell=best_sell,
                best_buy=best_buy,
                last_price=Decimal("0.3"),
                volume_24=Decimal("0.3"),
            )

    def test_price_within_range(self) -> None:
        """"""
        for price in BestPrice.objects.all():
            self.assertGreater(price.best_sell, price.best_buy)


class SnapshotViewTest(TestCase):
    """"""

    def test_view_url_exists_at_proper_location(self) -> None:
        """"""
        resp = self.client.get(reverse("order_app:snapshots"))
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self) -> None:
        """"""
        resp = self.client.get(reverse("order_app:snapshots"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        """"""
        resp = self.client.get(reverse("order_app:snapshots"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "order_app/snapshots.html")
