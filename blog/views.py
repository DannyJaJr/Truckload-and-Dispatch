from django.shortcuts import render
# Now importing the load fro function
from .models import Load

# Create your views here.

# function for the root page as home 
def home(request):
    # list_load created to store all the loads models
    list_loads = Load.objects.all()
    # the dictionaire context holds the data for Loads
    context={"list_loads": list_loads}
    # this function will return a index.html to render the call from urls.py path
    return render(request, "index.html", context)
