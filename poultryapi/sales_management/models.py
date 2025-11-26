from django.db import models
from users.models import User
   
class SalesManagement(models.Model): 
    
    created_by = models.ForeignKey(
        User,    
        on_delete=models.SET_NULL,       
        null=True,
        related_name='sales_management'  # <-- unique reverse name
    )        
    activity = models.CharField(max_length=200)   
    date = models.DateField(blank=True, null=True)
            