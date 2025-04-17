from django.db import models
from account.models import Account




class Order(models.Model):
    user = models.ForeignKey(to=Account, on_delete=models.CASCADE, verbose_name="User")
    origin_lat = models.FloatField(verbose_name="Origin Latitude")
    origin_lng = models.FloatField(verbose_name="Origin Longitude")
    destination_lat = models.FloatField(verbose_name="Destination Latitude")
    destination_lng = models.FloatField(verbose_name="Destination Longitude")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

  
    def __str__(self):
        return f"Order by {self.user} from ({self.origin_lat}, {self.origin_lng}) to ({self.destination_lat}, {self.destination_lng})"
