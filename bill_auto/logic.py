import models
import datetime

"""
This module will hold the business logic with which the views will use
"""     

def add_new_resident(name: str, birthday: datetime, admin_day: datetime, discharge_date: datetime, rent: int) -> None:
    tenant = models.Resident.objects.create(name=name,birthday=birthday,
                                            admission_date=admin_day,discharge_date=None,rent=rent)
    
