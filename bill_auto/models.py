from django.db import models

# Create your models here.
class Resident(models.Model):
    id = models.AutoField(primary_key=1)
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    admission_date = models.DateField()
    discharge_date = models.DateField(blank=True)
    rent = models.DecimalField(decimal_places=2,)