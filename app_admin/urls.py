from django.urls import include, path, re_path
from .views import *
from . import views


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('my-loads', user_loads, name="my-loads"),
    path('add-load', AddLoad.as_view(), name="add-load"),
    path('update-load/<int:pk>', UpdateLoad.as_view(), name="update-load"),
    # path('delete-load/<int:pk>', DeleteLoad.as_view(), name="delete-load"),
    path('delete_event/<event_id>', views.delete_event, name="delete-event"),

]



