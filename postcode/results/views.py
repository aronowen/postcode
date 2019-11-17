from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Service
from .models import Postcode
from .forms import t_filters

import math

def result(request):
    services = Service.objects.all()

    if request.method == 'POST':
        form = t_filters(request.POST)
        if form.is_valid():
            res_search = form.cleaned_data['postcode_input']
            for items in services:
                distance = haversine(res_search, services.lon, services.lat)
            form = t_filters()
            return render(request, 'result/result.html', {'services': services, 'form': form, 'distance':distance})
    else:
        form = t_filters()
        return render(request, 'result/result.html', {'services': services, 'form': form})

def haversine(postcode, lon, lat):
    R = 3958.8;
    postcode_obj = Service.objects.all()
    postcode_obj2 = Postcode.objects.get(postcode2=postcode)
    longitude1 = lon
    latitude1 = lat
    longitude2 = postcode_obj2.lon2 #53.2298
    latitude2 = postcode_obj2.lat2 #-4.12395

    print(f"{longitude1} | {latitude1} ", "TEST", " 53.143666 | -4.257318")
    print(f"{longitude2} | {latitude2} ", "TEST", " 53.2298 | -4.12395")

    rad_lon_1 = math.radians(longitude1)
    rad_lat_1 = math.radians(latitude1)
    rad_lon_2 = math.radians(longitude2)
    rad_lat_2 = math.radians(latitude2)

    delta_long = rad_lon_1-rad_lon_2;
    delta_lat = rad_lat_1-rad_lat_2;

    haversine_Theta = math.sin(delta_lat/2)**2 + math.cos(latitude1)*math.cos(latitude2)*math.sin(delta_long/2)**2;
    c = 2*math.atan2(math.sqrt(haversine_Theta), math.sqrt(1-haversine_Theta))

    result = R*c
    return result;
