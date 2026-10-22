from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class HealthEndpointTests(APITestCase):
    def test_health_returns_ok(self):
        response = self.client.get(reverse("health"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"status": "ok"})


class GreetingEndpointTests(APITestCase):
    def test_default_greeting(self):
        response = self.client.get(reverse("greeting"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["message"], "Hello, CSC325!")

    def test_greeting_with_name(self):
        response = self.client.get(reverse("greeting"), {"name": "Chris"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["message"], "Hello, Chris!")

    def test_greeting_rejects_post(self):
        response = self.client.post(reverse("greeting"))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
