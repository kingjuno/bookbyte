from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Req(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    url_id = models.SlugField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
