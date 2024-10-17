from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class InStock(models.Model):
    CompID = models.CharField(primary_key=True, max_length=20, unique=True)  
    Did = models.CharField(max_length=20)
    Comp = models.CharField(max_length=20)
    Btype = models.CharField(max_length=20)
    Coll = models.DateField()
    Exp = models.DateField()

    class Meta:
        db_table = 'instock'
        indexes = [
            models.Index(fields=['Did']),  
        ]

    def clean(self):
        if len(self.CompID) > 20:
            raise ValidationError("CompID cannot exceed 20 characters.")

        if len(self.Did) > 20:
            raise ValidationError("Did cannot exceed 20 characters.")
 
        if self.Exp < date.today():
            raise ValidationError("Expiry date cannot be in the past.")

    def save(self, *args, **kwargs):
        self.full_clean() 
        super().save(*args, **kwargs)  
