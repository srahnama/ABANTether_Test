from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=50, unique=True)
    currency = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    exchange_order_id = models.CharField(max_length=50, blank=True, null=True)
    exchange_response = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the order_id attribute.

        Returns:
            str: The string representation of the order_id attribute.
        """
        # Return the value of the order_id attribute
        return self.order_id
