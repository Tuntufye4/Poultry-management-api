from django.db import models

class  Inventory_movement(models.Model):      
    inventory_item = models.CharField(max_length=200)   
    movement_type = models.CharField(max_length=200)
    quantity = models.IntegerField()    
    date = models.DateField(blank=True, null=True)   
    reason = models.CharField(max_length=100)
       
                                        