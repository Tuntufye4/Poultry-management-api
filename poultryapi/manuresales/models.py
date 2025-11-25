from django.db import models

class  Manuresales(models.Model):      
    quantity_bags = models.IntegerField() 
    date = models.DateField(blank=True, null=True)     
    price_per_bag = models.IntegerField() 
    total_amount = models.IntegerField() 
    buyer_name = models.CharField(max_length=100)
       
                                                        