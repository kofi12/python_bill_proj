from django.db import models

# Create your models here.
class Resident(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    admission_date = models.DateField()
    discharge_date = models.DateField(blank=True, null=True)
    rent = models.DecimalField(decimal_places=2, max_digits=10)