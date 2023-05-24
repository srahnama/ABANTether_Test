from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Order
import requests
import json
from unittest.mock import patch

class OrderAPITests(APITestCase):
    def setUp(self):
        self.url = reverse('order-create')

      

    def test_create_order(self):
        data = {
            'order_id': '12345',
            'currency': 'ABAN',
            'amount': '10.0',
            'price': '50000.0',
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().order_id, '12345')
        self.assertIsNone(Order.objects.get().exchange_order_id)
        self.assertIsNone(Order.objects.get().exchange_response)

    

    def test_create_order_exchange_failure(self):
        # Test case for order creation when the exchange API call fails

        data = {
            'order_id': '12345',
            'currency': 'ABAN',
            'amount': '10.0',
            'price': '50000.0',
        }

        with patch('orders.views.requests.post') as mock_post:
            # Mock the exchange API response with an error status code
            mock_post.return_value.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

            response = self.client.post(self.url, data, format='json')

        # Assert the response and ensure no order is saved in the database
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(Order.objects.count(), 0)

    def test_list_orders(self):
        Order.objects.create(
            order_id='12345',
            currency='ABAN',
            amount='10.0',
            price='50000.0',
            exchange_order_id='67890',
            exchange_response='{"order_id": "67890", "status": "completed"}',
        )

        list_url = reverse('order-list')
        response = self.client.get(list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['order_id'], '12345')
        self.assertEqual(response.data[0]['exchange_order_id'], '67890')
        self.assertEqual(response.data[0]['exchange_response'], {
            'order_id': '67890',
            'status': 'completed',
        })