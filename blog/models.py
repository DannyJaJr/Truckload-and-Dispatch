from django.db import models
# to allow users acces on load model
from django.contrib.auth.models import User
from django.urls import reverse

from decouple import config
from twilio.rest import Client

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name




class Load(models.Model):
    # to allow users acces on loads
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=20)
    # price = models.IntegerField()
    title = models.CharField(max_length=50)
    # sync category with load, CASCADE allows deletion of relative
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField()
    image = models.ImageField(null=True, blank=True)
    # image=models.ImageField(upload_to="articles")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True)



    # now redifinition of the class to render the data by title
    def __str__(self):
        return self.title




    def get_absolute_url(sef):
        return reverse("my-loads")



    # def get_absolute_url(self):
    #     return reverse("my-loads")







class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.TextField()

    def __str__(self):
        return str(self.name)


    def save(self, *args, **kwargs):
        if(self.score != ""):
        # if self.score >= 0:
            account_sid = config('account_sid')
            auth_token = config('auth_token')
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"congratulation {self.name}, youscroenis {self.score}",
                from_= config('device_number'),
                to= config('my_number')
            )
        
        print(message.sid)
            
        return super().save( *args, **kwargs)






