from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name




class Load(models.Model):
    price = models.CharField(max_length=20)
    # price = models.IntegerField()
    title = models.CharField(max_length=50)
    # sync category with load, CASCADE allows deletion of relative
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField()
    image = models.ImageField()
    # image=models.ImageField(upload_to="articles")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True)



    # now redifinition of the class to render the data by title
    def __str__(self):
        return self.title


Load.objects.all()






