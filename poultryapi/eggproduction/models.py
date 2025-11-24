from django.db import models

class  Eggproduction(models.Model):      
    flock = models.CharField(max_length=200) 
    date = models.DateField(blank=True, null=True)     
    eggs_collected = models.CharField(max_length=200)
    cracked_eggs = models.CharField(max_length=200)    
    broken_eggs = models.CharField(max_length=200) 
    total_egg_weight_kg = models.CharField(max_length=200)   
    collector_name = models.CharField(max_length=100)

                              