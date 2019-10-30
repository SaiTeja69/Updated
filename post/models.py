from django.db import models
from django.conf import settings
# Create your models here.

user=settings.AUTH_USER_MODEL

class post(models.Model):
    user=models.ForeignKey(user,default=1,null=True,on_delete=models.SET_NULL)
    title=models.CharField(max_length=30)
    slug=models.SlugField(unique=True)
    image=models.ImageField(upload_to='images/',blank=True,null=True)
    description=models.TextField()
