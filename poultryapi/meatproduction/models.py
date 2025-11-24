from django.db import models

class  Meatproduction(models.Model):      
    flock = models.CharField(max_length=200)   
    date = models.DateField(blank=True, null=True)   
    sample_size = models.IntegerField()
    average_weight_kg = models.IntegerField()  
    lowest_weight_kg = models.IntegerField()    
    highest_weight_kg = models.IntegerField() 
                                               