from django.db import models
from user.models import CustomUser

class Auction(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
    highest_bid = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    auction_id = models.AutoField(primary_key=True)
    

    
    def __str__(self):
        return self.item_name
    
    
