from django.db import models
from users.models import User

class  Inventory_movement(models.Model):    
    created_by = models.ForeignKey(
        User,    
        on_delete=models.SET_NULL,
        null=True,
        related_name='inventory_movement'  # <-- unique reverse name
    )        
    inventory_item = models.CharField(max_length=200)   
    movement_type = models.CharField(max_length=200)
    quantity = models.IntegerField()    
    date = models.DateField(blank=True, null=True)   
    reason = models.CharField(max_length=100)
    movement_status = models.CharField(max_length=100, blank=True, null=True)
       
                                        