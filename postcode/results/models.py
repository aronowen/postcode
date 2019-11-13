from django.db import models
from datetime import datetime

class Service(models.Model):
    name = models.CharField(max_length=225)
    distance = models.CharField(max_length=225)
    OWNER = [
        ('NHS', 'NHS'),
        ('Private', 'Private'),
    ]
    owner = models.CharField(max_length=500, choices=OWNER)
    doctor = models.BooleanField(default=True)
    dentist = models.BooleanField(default=True)
    optician = models.BooleanField(default=True)
    address = models.CharField(max_length=225)
    postcode = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    lon = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    lat = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    create_date = models.DateTimeField(null=False)



    def __str__(self):
        return self.name


    def summary(self):
        return self.description[:225]


    def create_date_display(self):
        return self.create_date.strftime('%e %b %y')
