from django.db import models
from users.models import User

class Expenses(models.Model): 
    created_by = models.ForeignKey(
        User,    
        on_delete=models.SET_NULL,       
        null=True,
        related_name='expenses'  # <-- unique reverse name
    )        
    expense_type = models.CharField(max_length=200)   
    flock = models.CharField(max_length=200)  
    amount = models.FloatField()
    date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=200)    
    paid_by = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100) 
       


        
                                                     