from django.shortcuts import render

# Create your views here.

# function for the root page as home 
def home(request):
    # this function will return a index.html to render the call from urls.py path
    return render(request, "index.html")
