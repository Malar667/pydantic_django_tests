from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse

from stats.tests.factories import AuthorFactory
from stats.tests.mock_data import AUTHORS_INPUT


class TestApiPerformance(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.authors = AuthorFactory.create_batch(size=5000)
        cls.author = cls.authors[0]

    def test_drf_create(self):
        url = reverse("stats:drf-performance-create")

        response = self.client.post(
            url, data=AUTHORS_INPUT, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_drf_detail(self):
        url = reverse("stats:drf-performance-single")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_drf_list(self):
        url = reverse("stats:drf-performance-list")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_djantic_create(self):
        url = reverse("stats:djantic-performance-create")

        response = self.client.post(
            url, data=AUTHORS_INPUT, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_djantic_details(self):
        url = reverse("stats:djantic-performance-single")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_djantic_list(self):
        url = reverse("stats:djantic-performance-list")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ninja_create(self):
        raise NotImplementedError()

    def test_ninja_details(self):
        raise NotImplementedError()

    def test_ninja_list(self):
        raise NotImplementedError()
