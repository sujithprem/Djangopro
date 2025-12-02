from django.urls import path
from .views import *

urlpatterns = [
    path('shop', get_all_data, name='shop'),
]
