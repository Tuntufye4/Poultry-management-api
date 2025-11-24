from django.db import models

class Treatment(models.Model):      
    flock = models.CharField(max_length=200)   
    date = models.DateField(blank=True, null=True)
    treatment_type = models.CharField(max_length=200)    
    drug_name = models.CharField(max_length=100)
    dosage_per_liter = models.CharField(max_length=100)  
    total_quantity_used = models.CharField(max_length=100)
    administered_by = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
                                                         