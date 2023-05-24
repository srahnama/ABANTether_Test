from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Order
from django.db.models import Sum
import requests

@receiver(post_save, sender=Order)
def buy_from_exchange(sender, instance, created, **kwargs):
     if created:
        # Calculate the sum of amounts for the last instances with null exchange_order_id
        total_amount = Order.objects.filter(exchange_order_id__isnull=True).exclude(id=instance.id).aggregate(total=Sum('amount'))['total']

        # Check if the total amount is greater than or equal to $10
        if total_amount and total_amount >= 10.0:
            # Replace the following URL and headers with your actual exchange API details
            url = settings.EXCHANGE_API_URL + '/buy'
            headers = {
                'Authorization': 'Bearer ' + settings.EXCHANGE_API_TOKEN,
                'Content-Type': 'application/json',
            }

            # Prepare the payload to send to the exchange API
            payload = {
                'order_id': instance.order_id,
                'currency': instance.currency,
                'amount': instance.amount,
                'price': instance.price,
            }

            # Send the request to the exchange API
            response = requests.post(url, headers=headers, json=payload)

            # Check if the request was successful
            if response.status_code == requests.codes.ok:
                # Extract the exchange API response
                exchange_response = response.json()

                # Update the exchange-related fields in the Order instance
                instance.exchange_order_id = exchange_response['order_id']
                instance.exchange_response = exchange_response

                # Save the updated instance
                instance.save()