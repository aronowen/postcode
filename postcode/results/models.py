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


    #def postcode_validate(postcode):
    #    check = re.search("^([A-PR-UWYZ](([0-9](([0-9]|[A-HJKSTUW])?)?)|([A-HK-Y][0-9]([0-9]|[ABEHMNPRVWXY])?)) ?[0-9][ABD-HJLNP-UW-Z]{2})$", postcode);
    #    if check is None :
    #        return False;
    #    else :
    #        return True;


class Service(models.Model):
    name = models.CharField(max_length=225)
    distance = models.FloatField()
    OWNER = [
        ('NHS', 'NHS'),
        ('Private', 'Private'),
    ]
    owner = models.CharField(max_length=500, choices=OWNER)
    doctor = models.BooleanField(default=False)
    dentist = models.BooleanField(default=False)
    optician = models.BooleanField(default=False)
    address = models.CharField(max_length=225)
    postcode = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    lon = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    lat = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    create_date = models.DateTimeField(null=False)

    def __str__(self):
        return self.name

    def haversine(self):
        R = 3958.8;
        postcode_obj = Postcode.objects.get(postcode2='LL57 1UT')
        longitude1 = self.lon
        latitude1 = self.lat
        longitude2 = postcode_obj.lon2 #53.2298
        latitude2 = postcode_obj.lat2 #-4.12395

        print(postcode_obj.lat2)

        rad_lon_1 = math.radians(longitude1)
        rad_lat_1 = math.radians(latitude1)
        rad_lon_2 = math.radians(longitude2)
        rad_lat_2 = math.radians(latitude2)

        delta_long = rad_lon_1-rad_lon_2;
        delta_lat = rad_lat_1-rad_lat_2;

        haversine_Theta = math.sin(delta_lat/2)**2 + math.cos(latitude1)*math.cos(latitude2)*math.sin(delta_long/2)**2;
        c = 2*math.atan2(math.sqrt(haversine_Theta), math.sqrt(1-haversine_Theta))

        result = R*c
        self.distance = result;
        return self.distance;

    def create_date_display(self):
        return self.create_date.strftime('%e %b %y')
