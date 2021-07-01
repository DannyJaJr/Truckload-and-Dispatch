from django.shortcuts import render

# Create your views here.
# # function pout admin
def dashboard(request):
    return render(request, 'db.html')