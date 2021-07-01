from django.shortcuts import render, redirect
from blog.models import Load
# for CRUD rendering
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from blog.forms import LoadForm

# Create your views here.
# # function pout admin
def dashboard(request):
    return render(request, 'db.html')


# funtion to display user loads
def user_loads(request):
    if not request.user.is_authenticated:
        return rredirect('login')
    list_loads = Load.objects.filter(user= request.user)
    return render(request, 'my-loads.html', {'list_loads': list_loads})



########### class 
# class to add a load
class AddLoad(CreateView):
    model = Load
    form_class = LoadForm
    # to display where the form will be render
    template_name = "add-load.html"
    success_url = "my-loads"

    def form_valid(self, form):
        # form_valid allows only authorized users
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateLoad(UpdateView):
    model = Load
    form_class =LoadForm
    # to force Django to look for the right template, because the default value was blog/load_form.html
    template_name = 'app_admin/load_form.html'
    success_url = '/my-admin/my-loads'



