"""

"""
from random import randint

from django.test import TestCase
from django.urls import reverse

from .models import BestPrice


class BestPriceLTVModelTest(TestCase):
    """"""

    def setUp(self):
        """Fill in our test database's table"""
        price_range = (300, 900)  # Spread for test set
        # Get arithmetic mean value
        mean = int((price_range[1] - price_range[0]) / 2)
        for i in range(40):
            best_sell = randint(mean,price_range[1])  # From middle to high
            best_buy = randint(price_range[0], mean)  # From low to middle
            # TODO: refresh seed
            BestPrice.objects.create(best_sell=best_sell,
                                     best_buy=best_buy)

    def test_price_within_range(self):
        """"""
        for price in BestPrice.objects.all():
            self.assertGreater(price.best_sell, price.best_buy)


class SnapshotViewTest(TestCase):
    """"""

    def setUp(self):
        """"""
        pass

    def test_view_url_exists_at_proper_location(self):
        """"""
        resp = self.client.get(reverse("snapshots"))
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        """"""
        resp = self.client.get(reverse("snapshots"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        """"""
        resp = self.client.get(reverse("snapshots"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "snapshots.html")
