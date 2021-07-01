from django.urls import include, path
from .views import *


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('my-loads', user_loads, name="my-loads")
]
