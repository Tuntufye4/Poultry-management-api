from django.db import models

class Nutrition(models.Model):      
    flock = models.CharField(max_length=200)   
    feed_type = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    feed_brand = models.CharField(max_length=200)    
    quantity_kg = models.CharField(max_length=100)
    cost_per_kg = models.CharField(max_length=100)  
    notes = models.CharField(max_length=100)
    total_cost = models.CharField(max_length=100)
    
                                   