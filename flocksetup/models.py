from django.db import models
from users.models import User  

class Flocksetup(models.Model):  
    created_by = models.ForeignKey(
        User,    
        on_delete=models.SET_NULL,
        null=True,
        related_name='flocksetup'  # <-- unique reverse name
    )       
    poultry_house = models.CharField(max_length=200)   
    breed = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    arrival_date = models.DateField(blank=True, null=True)
    initial_quantity = models.IntegerField()    
    age_in_days_at_arrival = models.IntegerField()     
    source_supplier = models.CharField(max_length=100)  
    cost_per_bird = models.FloatField() 
                              