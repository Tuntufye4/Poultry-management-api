from django.db import models

class Expenses(models.Model):      
    expense_type = models.CharField(max_length=200)   
    flock = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=200)    
    paid_by = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)  
    
                                      