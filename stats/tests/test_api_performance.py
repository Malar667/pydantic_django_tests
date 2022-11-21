from django.test import TestCase
from rest_framework.reverse import reverse

from stats.tests.factories import AuthorFactory


class TestApiPerformance(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.authors = AuthorFactory.create_batch(size=5000)
        cls.author = cls.authors[0]

    def test_drf_create(self):
        pass

    def test_drf_detail(self):
        url = reverse("stats:drf-performance-single", args=[self.author.id])

        self.client.get(url)

    def test_drf_list(self):
        url = reverse("stats:drf-performance-list")

        self.client.get(url)

    def test_ninja_create(self):
        pass

    def test_djantic_details(self):
        pass

    def test_djantic_list(self):
        pass

    def test_ninja_create(self):
        pass

    def test_ninja_details(self):
        pass

    def test_ninja_list(self):
        pass
