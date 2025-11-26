from django.db import models
from users.models import User                 

class Culling(models.Model):   
    created_by = models.ForeignKey(
        User,    
        on_delete=models.SET_NULL,
        null=True,
        related_name='culling'  # <-- unique reverse name
    )   
    flock = models.CharField(max_length=200)   
    date = models.DateField(blank=True, null=True)
    quantity_sold = models.CharField(max_length=200)    
    weight_per_bird_kg = models.IntegerField()
    price_per_bird = models.FloatField()           
    total_amount = models.FloatField()
    buyer_name = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
                                                          