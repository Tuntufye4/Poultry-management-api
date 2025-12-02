from django.db import models
from users.models import User

class  Meatproduction(models.Model): 
    created_by = models.ForeignKey(
        User,    
        on_delete=models.SET_NULL,
        null=True,
        related_name='meatproduction'  # <-- unique reverse name
    )        
    flock = models.CharField(max_length=200)   
    date = models.DateField(blank=True, null=True)   
    sample_size = models.IntegerField()
    average_weight_kg = models.IntegerField()  
    lowest_weight_kg = models.IntegerField()    
    highest_weight_kg = models.IntegerField()    
                