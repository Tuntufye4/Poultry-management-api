from django.db import models
from users.models import User

class  Meatsales(models.Model):
    created_by = models.ForeignKey(
        User,        
        on_delete=models.SET_NULL,
        null=True,
        related_name='meatsales'  # <-- unique reverse name
    )         
    flock = models.CharField(max_length=200) 
    date = models.DateField(blank=True, null=True)     
    kgs_sold = models.IntegerField()     
    price_per_kg = models.FloatField()    
    total_amount = models.FloatField() 
    buyer_name = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)   
    chicken_type = models.CharField(max_length=100, blank=True)
    processing_type = models.CharField(max_length=100, blank=True)