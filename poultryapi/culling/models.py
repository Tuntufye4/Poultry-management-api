from django.db import models

class Culling(models.Model):      
    flock = models.CharField(max_length=200)   
    date = models.DateField(blank=True, null=True)
    quantity_sold = models.CharField(max_length=200)    
    weight_per_bird_kg = models.IntegerField()
    price_per_bird = models.IntegerField()  
    total_amount = models.IntegerField()
    buyer_name = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
                                                        