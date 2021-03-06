# from django.shortcuts import render
# Now importing the load fro function
from .models import Load, Message
# edit app_auth
from django.shortcuts import render, redirect
# for authentication now let import django.contrib
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# to import all types of forms such as login , register
from .forms import *
from twilio.rest import Client

# Create your views here. GET POST META method
########### Functions ###################################
# function for the root page as home 
def home(request):
    # list_load created to store all the loads models
    list_loads = Load.objects.all()
    # the dictionaire context holds the data for Loads
    context={"list_loads": list_loads}
    # this function will return a index.html to render the call from urls.py path
    return render(request, "index.html", context)


# function that work with the route located in truckload/urls.py
# path('/load/<int:id_load>', detail, name="detail" )
# to render the page detail.html to read card button "read"
def detail(request, id_load):
    # print("the load id is: " , id_load)
    load=Load.objects.get(id=id_load)
    # load=Load.objects.get(id=id_load) is tested on the shell by 'Load.objects.all()' and  Load.objects.get(id=1)
    # :[:5] => to limit the lods displyed related to 6 
    category = load.category
    loads_in_relation = Load.objects.filter(category =  category)[:6]
    return render(request, 'detail.html', {"load": load, "lir": loads_in_relation})



#function for the search bar on the vav header
def search(request):
    # the attribut will interset the the value from the form search to incorporate these value as  a GET
    query= request.GET["load"]
     # SELECT * FROM load where title like '%'+query+  => https://docs.djangoproject.com/en/3.2/ref/request-response/
    # icontains  allows non sesnsitive case while contains rpvide sensitive case search 
    list_load = Load.objects.filter(desc__contains = query)
    # list_details = Load.objects.filter(desc__contains = query)
    return render(request, "search.html", {"list_load": list_load})
# query stands for the request the database may start whit anything 



# function to recieve sms  https://www.youtube.com/watch?v=KYQ3u3xDPRA
def sms(request):
    message = request.GET['body']
    # to separate the message into 2 parts
    message_splited = message.split("-")
    # to set the first part of the array as title
    title = message_splited[0]
    # to set the 2nd part of the array as description
    desc = message_splited[1]

    agri_category = Category.objects.get(id = 2)
    load = Load(title = title, category = agri_category, desc = desc, image = "http://default")
    load.save()
    print('data saved succesfully')
    return HttpResponse("data saved succesfully")

def message(request):
    message = request.GET('body')
    # to separate the message into 2 parts
    message_splited = message.split("-")
    # to set the first part of the array as title
    title = message_splited[0]
    # to set the 2nd part of the array as description
    desc = message_splited[1]
    agri_category = Category.objects.get(id = 2)
    load = Load(title = title, category = agri_category, desc = desc, image = "http://default")
    load.save()
    print('data saved succesfully')
    return HttpResponse("data saved succesfully")




# function for loggin
def loging_blog(request):
    if request.method == "POST":
        form = LoginForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Your email address and password combination do not match any of our accounts.')
                return render(request, 'login.html', {'form':form})
        else:  
            # for field in form.errors:
            #     # to render the form input in colors 
            #     form[field].field.widget.attrs['class'] += 'is-invalid'
                # ['class'] += 'is-invalid' is class from bootstrap
            return render(request, 'login.html', {'form':form})
            
            
            
            
    else:
        form = LoginForm()
        return render(request, "login.html", {"form":form })



# function to create an account
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user =User.objects.create_user(username=username, password = pwd)
            if user is not None:
                return redirect("login-blog")
            else:
                messages.error(request, 'Creation failure')
                return render(request, 'register.html', {'form':form})
        else:
            return render(request, 'register.html', {'form':form})
                



        return render(request, 'register.html', {})
    
    form = RegisterForm()
    return render(request, 'register.html', {'form':form})



# function to log out users
def logout_blog(request):
    logout(request)
    return redirect('login-blog')







### function to send sms for load requirements
def PhoneNumber(request):
    myphone = request.POST.get('phone')
    bid = request.POST.get('bid')

    def __str__(self):
        return '{} {}' .format(self.myphone, self.bid ) 
        # return self.myphone, self.bid

    def save(self, *args, **kwargs):
        if self.bid > 0:
            account_sid = ''
            auth_token = ''
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body='We agreed about your bid, and will send you the load agreement and information- {self.bid}',
                from_='+',
                to='{self.myphone}'
            )
            print(message.sid)
            return super().save(*args, **kwargs) 
       
        
            
            
        
      