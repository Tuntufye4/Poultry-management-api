from django.db import models
from users.models import User

class Treatment(models.Model):  
    created_by = models.ForeignKey(
        User,    
        on_delete=models.SET_NULL,   
        null=True,
        related_name='treatments'  # <-- unique reverse name
    )       
    flock = models.CharField(max_length=200)   
    date = models.DateField(blank=True, null=True)
    treatment_type = models.CharField(max_length=200)    
    drug_name = models.CharField(max_length=100)
    drug_type = models.CharField(max_length=100, blank=True, null=True)
    dosage_per_liter = models.IntegerField()  
    total_quantity_used = models.IntegerField()
    administered_by = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
                                                            