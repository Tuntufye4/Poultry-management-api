from django.db import models
from users.models import User
   
class LogisticsManagement(models.Model): 
    
    created_by = models.ForeignKey(
        User,    
        on_delete=models.SET_NULL,       
        null=True,
        related_name='logistics_management'  # <-- unique reverse name
    )        
    activity = models.CharField(max_length=200)   
    date = models.DateField(blank=True, null=True)
         