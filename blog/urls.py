from django.urls import path
# import view to render the functions
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # the view.py will call the function 'home' to render in templates for the "/" path
    path('', views.home, name='home'),
    
]