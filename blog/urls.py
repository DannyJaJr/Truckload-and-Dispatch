from django.urls import include, path
# import view to render the functions
from . import views
# edit app_auth
from .views import *

urlpatterns = [
    
     # corecteted path from blog
    path('', views.home, name='home'),
    path('login', loging_blog, name='login-blog'),
    path('register', register, name='register'),
    path('logout', logout_blog, name='logout'),
]



