from django.db import models

class  Inventory(models.Model):      
    category = models.CharField(max_length=200)   
    item_name = models.CharField(max_length=200)
    quantity = models.IntegerField()    
    unit = models.IntegerField() 
    unit_price = models.IntegerField()
    expiry_date = models.DateField(blank=True, null=True)   
    supplier = models.CharField(max_length=100)
    source_supplier = models.CharField(max_length=100)  
    last_restock_date = models.DateField(blank=True, null=True)
                              