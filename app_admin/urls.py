from django.urls import include, path
from .views import *


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('my-loads', user_loads, name="my-loads"),
    path('add-load', AddLoad.as_view(), name="add-load"),
]



