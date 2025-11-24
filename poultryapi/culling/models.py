from django.db import models

class Culling(models.Model):      
    flock = models.CharField(max_length=200)   
    date = models.DateField(blank=True, null=True)
    quantity_sold = models.CharField(max_length=200)    
    weight_per_bird_kg = models.CharField(max_length=100)
    price_per_bird = models.CharField(max_length=100)  
    total_amount = models.CharField(max_length=100)
    buyer_name = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
                                                    