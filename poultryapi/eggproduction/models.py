from django.db import models
from users.models import User 

class  Eggproduction(models.Model):     
    created_by = models.ForeignKey(
        User,    
        on_delete=models.SET_NULL,
        null=True,
        related_name='eggproduction'  # <-- unique reverse name
    )        
    flock = models.CharField(max_length=200) 
    date = models.DateField(blank=True, null=True)     
    eggs_collected = models.IntegerField()
    cracked_eggs = models.CharField(max_length=200)    
    broken_eggs = models.CharField(max_length=200) 
    total_egg_weight_kg = models.IntegerField()   
    collector_name = models.CharField(max_length=100)

                                              


                                               