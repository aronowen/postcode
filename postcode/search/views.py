from django.shortcuts import render
from .forms import SearchForm

def home(request):
        return render(request, 'home/home.html')
