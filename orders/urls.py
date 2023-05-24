from django.urls import path
from orders.views import OrderCreateAPIView, OrderListAPIView

urlpatterns = [
    path('api/orders/', OrderCreateAPIView.as_view(), name='order-create'),
    path('api/orders/list/', OrderListAPIView.as_view(), name='order-list'),
]