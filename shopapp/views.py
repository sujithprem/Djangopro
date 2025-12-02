from django.shortcuts import render
from .models import *

# Create your views here.

def get_all_data(request):
    products = dressinfoTable.objects.all()
    return render(request, 'shop.html',{"products":products})