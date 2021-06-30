# from django.shortcuts import render, redirect

# # for authentication now let import django.contrib
# from django.contrib.auth import authenticate
# from django.contrib import messages

# # Create your views here.
# def loging_blog(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         pwd = request.POST['pwd']
#         user = authenticate(username = username, password = pwd)
#         # if user doesn't exist we use the redirect from from django.shortcuts
#         if user is not None:
#             return redirect("home")
#         else:
#             messages.error(request, "Your email address and password combination do not match any of our accounts.")
#             return render(request, "login.html")


#     return render(request, "login.html")


    
    
