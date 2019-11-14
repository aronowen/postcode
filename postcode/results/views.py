from django.shortcuts import render
from .models import Service
import math

def result(request):
    services = Service.objects.all()
    return render(request, 'result/result.html', {'services': services})
