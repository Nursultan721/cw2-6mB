from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class EndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_stats_endpoint(self):
        response = self.client.get('/api/v1/stats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"users_count": 1000, "active_orders": 42})

    def test_register_endpoint(self):
        response = self.client.post('/api/v1/register/', {'email': 'test@example.com'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)