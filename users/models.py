from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import datetime


# Create your models here.

class Profile (models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date=models.DateField(null=True)
    phone_number=models.CharField(max_length=15)
    country=models.ForeignKey('Country',related_name='country',on_delete=models.CASCADE,blank=True, null=True)
    image=models.ImageField(upload_to='profile_img',blank=True, null=True)
    slug=models.SlugField(null=True, blank=True,unique=True)
    join_date=models.DateTimeField(blank=True, default=datetime.datetime.now)

    def __str__(self):
        return self.user.username
    
    def save(self,*args ,**kwargs):
        if not self.slug:
            self.slug=slugify(self.user.username)
        super(Profile, self).save(*args ,**kwargs)
    


class Country (models.Model):
    name=models.CharField(max_length=20)
    def __str__(self) :
        return self.name

