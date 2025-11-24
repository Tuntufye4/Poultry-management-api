from django.db import models

class Flocksetup(models.Model):      
    poultry_house = models.CharField(max_length=200)   
    breed = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    arrival_date = models.DateField(blank=True, null=True)
    initial_quantity = models.CharField(max_length=200)    
    age_in_days_at_arrival = models.CharField(max_length=100)
    source_supplier = models.CharField(max_length=100)  
    cost_per_bird = models.CharField(max_length=100) 
                          