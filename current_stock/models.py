from django.db import models
from users.models import User

class  Currentstock(models.Model):        
    created_by = models.ForeignKey(
        User,        
        on_delete=models.SET_NULL,
        null=True,
        related_name='current_stock'  # <-- unique reverse name
    )         
    dressed = models.IntegerField()     
    undressed = models.IntegerField()          
    chicken_parts = models.IntegerField()  
    manure_bags = models.IntegerField()
    chicken_packaging_type = models.CharField(max_length=100)  
    manure_packaging_type = models.CharField(max_length=100) 
    chicken_feed = models.IntegerField(blank=True, null=True)   


                                                              