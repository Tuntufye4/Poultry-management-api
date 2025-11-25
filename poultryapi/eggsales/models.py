from django.db import models

class  Eggsales(models.Model):      
    flock = models.CharField(max_length=200) 
    date = models.DateField(blank=True, null=True)     
    trays_sold = models.IntegerField()
    price_per_tray = models.FloatField()    
    total_amount = models.FloatField() 
    buyer_name = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
                                                        