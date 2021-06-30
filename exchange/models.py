from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=100)
    bk = models.CharField(max_length=100,blank=True)
    message = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,default=None,on_delete=models.CASCADE,related_name="c1")
    client=models.ForeignKey(User,default=None,on_delete=models.CASCADE,related_name="c2")
    


    def __str__(self):
        return self.location
