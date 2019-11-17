from django.shortcuts import render
from .models import Service

def result(request):
    services = Service.objects.all()
    return render(request, 'result/result.html', {'services': services})
