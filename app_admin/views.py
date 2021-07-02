from django.shortcuts import render, redirect
from blog.models import Load
# for CRUD rendering
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from blog.forms import LoadForm
from django.urls import reverse
from django.core.exceptions import PermissionDenied
# implemented authentication on classes
from django.contrib.auth.mixins import LoginRequiredMixin
# implemented authentication on  functions
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render





# Create your views here.
# # function pout admin
def dashboard(request):
    return render(request, 'db.html')


# funtion to display user loads
@login_required
def user_loads(request):
    if request.user.has_perm("blog.delete_load"):
        print("You don't have the right")
    else:
        print("Access granted for deletiont")
    
    list_loads = Load.objects.filter(user= request.user)
    return render(request, 'my-loads.html', {'list_loads': list_loads})



########### class 
# class to add a load
class AddLoad(LoginRequiredMixin  ,CreateView):
    model = Load
    form_class = LoadForm
    # to display where the form will be render
    template_name = "add-load.html"
    success_url = "my-loads"

    def form_valid(self, form):
        # form_valid allows only authorized users
        form.instance.user = self.request.user
        return super().form_valid(form)

# class to update loads
class UpdateLoad(LoginRequiredMixin ,UpdateView):
    model = Load
    form_class =LoadForm
    template_name = 'app_admin/load_form.html'
    # return reverse("updateload", kwargs={"slug": self.slug})
    # success_url = '/my-admin/my-loads'

  

# # class to delete a load
# class DeleteLoad(DeleteView):
#     model = Load
#     success_url = "/my-loads"


# def delete_load(request, load_id):



def delete_event(request, event_id):
    event = Load.objects.get(pk=event_id)
    event.delete()
    return redirect("my-loads")

# def DeleteLoad(request,  event_id):
#     event = Event,objects.get(pk=event_id)
#     event.delete()
#     return redirect("my-load")


# Raising a 404
def dispath(self, request, *args, **kwargs):
    if not request.user.has_perm('blog.delete_load'):
        raise Http404("Permission Denied")
        return super().dispath(request, *args, **kwargs)



        
    

  





