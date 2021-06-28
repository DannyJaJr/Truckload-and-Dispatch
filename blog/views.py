from django.shortcuts import render
# Now importing the load fro function
from .models import Load

# Create your views here.
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
    return render(request, 'detail.html', {"load": load})