from django.db import models

class  Meatproduction(models.Model):      
    flock = models.CharField(max_length=200)   
    date = models.DateField(blank=True, null=True)   
    sample_size = models.CharField(max_length=100)
    average_weight_kg = models.CharField(max_length=100)  
    lowest_weight_kg = models.CharField(max_length=100) 
    highest_weight_kg = models.CharField(max_length=100) 
                                          