from django.db import models

class Flocksetup(models.Model):      
    poultry_house = models.CharField(max_length=200)   
    breed = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    arrival_date = models.DateField(blank=True, null=True)
    initial_quantity = models.IntegerField()    
    age_in_days_at_arrival = models.IntegerField()     
    source_supplier = models.CharField(max_length=100)  
    cost_per_bird = models.IntegerField() 
                              