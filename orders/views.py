from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
import requests

# Create your views here.
class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
  
class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Make the buy request to the exchange API
        response = self.buy_from_exchange(serializer.validated_data)
        if response.status_code != status.HTTP_200_OK:
            return Response({'error': 'Failed to buy from the exchange.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Save the exchange details in the order
        serializer.validated_data['exchange_order_id'] = response.json().get('order_id')
        serializer.validated_data['exchange_response'] = response.json()

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def buy_from_exchange(self, order_data):
        # Adjust the following code based on your exchange API integration
        endpoint = settings.EXCHANGE_API_URL + '/buy'
        data = {
            'currency': order_data['currency'],
            'amount': order_data['amount'],
            'price': order_data['price'],
        }
        headers = {
            'Authorization': 'Bearer ' + settings.EXCHANGE_API_TOKEN,
        }
        response = requests.post(endpoint, json=data, headers=headers)
        return response