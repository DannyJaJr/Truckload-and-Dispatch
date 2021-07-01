from django.urls import include, path
# import view to render the functions
from . import views
# edit app_auth
from .views import *

urlpatterns = [
    # path('', views.index, name='index'),
    # the view.py will call the function 'home' to render in templates for the "/" path
    path('', views.home, name='home'),
    path('login', loging_blog, name='login-blog'),
    path('register', register, name='register'),
    path('logout', logout_blog, name='logout'),
    
]



# from django.urls import include, path
# # from blog.views import home, detail, search, 

# from .views import loging_blog

# urlpatterns = [
#     path('login', loging_blog, name='login-blog')
# ]