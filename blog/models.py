from django.db import models

# Create your models here.
class Load(models.Model):
    price = models.CharField(max_length=20)
    # price = models.IntegerField()
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField()
    # image=models.ImageField(upload_to="articles")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True)

    # now redifinition of the class to render the data by title
    def __str__(self):
        return self.title
