from django.db import models
from django.contrib.auth.models import User

class Cars(models.Model):
    title = models.CharField(max_length=250)
    parametrs = models.TextField()
    color = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cars', blank=True, null=True)
    price = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title