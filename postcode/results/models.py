from django.db import models
from datetime import datetime
import math, re

class Postcode(models.Model):
    street_name = models.CharField(max_length=225)
    postcode2 = models.CharField(max_length=225)
    lon2 = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    lat2 = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    create_date = models.DateTimeField(null=False)


    def __str__(self):
        return f"| {self.street_name} | {self.postcode2} |"


class Service(models.Model):
    name = models.CharField(max_length=225)
    distance = models.FloatField(default=1)
    OWNER = [
        ('NHS', 'NHS'),
        ('Private', 'Private'),
    ]
    owner = models.CharField(max_length=500, choices=OWNER)
    TYPE=[('Doctors','Doctors'),
          ('Nursery', 'Nursery'),
          ('Dentists','Dentists'),
          ('Optometrists', 'Optometrists')]
    type = models.CharField(max_length=500, choices=TYPE)
    address = models.CharField(max_length=225)
    postcode = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    lon = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    lat = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    create_date = models.DateTimeField(null=False)


    def __str__(self):
        return self.name


    def create_date_display(self):
        return self.create_date.strftime('%e %b %y')
