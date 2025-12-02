from django.db import models
from users.models import User

class  Manuresales(models.Model):   
    created_by = models.ForeignKey(
        User,    
        on_delete=models.SET_NULL,
        null=True,
        related_name='manuresales'  # <-- unique reverse name
    )      
    quantity_bags = models.IntegerField() 
    date = models.DateField(blank=True, null=True)     
    price_per_bag = models.FloatField() 
    total_amount = models.FloatField() 
    buyer_name = models.CharField(max_length=100)          
    payment_method = models.CharField(max_length=100)   
    manure_type = models.CharField(max_length=100, blank=True, null=True)
    manure_quality = models.CharField(max_length=100, blank=True, null=True)
       
                                                            