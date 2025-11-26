from django.db import models
from users.models import User

class  Inventory(models.Model):
    created_by = models.ForeignKey(
        User,    
        on_delete=models.SET_NULL,
        null=True,
        related_name='inventory'  # <-- unique reverse name
    )             
    category = models.CharField(max_length=200)   
    item_name = models.CharField(max_length=200)
    quantity = models.IntegerField()    
    unit = models.IntegerField()    
    unit_price = models.FloatField()
    expiry_date = models.DateField(blank=True, null=True)   
    supplier = models.CharField(max_length=100)
    source_supplier = models.CharField(max_length=100)  
    last_restock_date = models.DateField(blank=True, null=True)
                              