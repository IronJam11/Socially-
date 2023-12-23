from django.db import models
from django.utils import timezone
from django.conf import settings 

# Create your models here.
class RegisterUser(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    published_date = models.DateTimeField(blank=True, null=True)
    image_url = models.ImageField(blank=True)
    
    
    def __str__(self):
        return self.username
    def upload(self):
        self.published_date= timezone.now()
        self.save()
        
class LoginUser(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
        
    def __str__(self):
        return self.username
        
class Sample(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
        
    def __str__(self):
        return self.username
        
class Blog(models.Model):
    type = models.CharField(max_length=25)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    published_date = models.DateTimeField(blank=True,null = True)
    
class Post(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField()
    caption = models.CharField(max_length = 200)
    likes = models.IntegerField()
    
    
    
    
    
    
        
