"""truckload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.urls import include, path
# # from blog.views import home, detail, search, 

# from .views import loging_blog

# urlpatterns = [
#     path('login', loging_blog, name='login-blog')
# ]





from django.contrib import admin
from django.urls import path, include
# bring views to create the path for home, deatail, search, sms
from blog.views import home, detail, search, sms, message, loging_blog
# from blog.views import home, detail, search, sms, message, loging_blog, phoneFunction
#  to render static file documentation (https://docs.djangoproject.com/en/3.2/howto/static-files/)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('loging/', include("django.contrib.auth.urls")), new
    
    # 1 the main root path of my app is set to blog
    # path('', include("blog.urls")),
    # 2 now import home function from view
    path('', home, name="home"),
    # the "<> allows to call any id, the int: allows only integer parsing"
    path('load/<int:id_load>', detail, name="detail" ),
    # for the search form on the nav bar
    path('load/research', search, name="search" ),
    # to recieve data from android and to start development server at http://127.0.0.1:8000/
    path('message-sms', sms, name="sms"),
    path('message-text', message, name="message"),


    
    


    path('auth/', include("blog.urls")),
    path('my-admin/', include("app_admin.urls")),
    # path('login', loging_blog, name='login-blog')


    ########path for phone access
    


    
    
    # https://docs.djangoproject.com/en/3.2/howto/static-files/ for storage image from the settings
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# http://192.168.0.12:8000/message-sms     my ip is 192.168.0.12
# python3 manage.py runserver 0.0.0.0:8000 allows the server to run all ips range
# http://192.168.0.12:8000/message-sms?body = content or titlt - body of the message