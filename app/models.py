from embed_video.fields import EmbedVideoField
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.


class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):  # sourcery skip: use-fstring-for-concatenation
        return self.name + ": " + str(self.videofile)

    

    
    
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    anime_watched=models.CharField( max_length=250)
    
    def __str__(self) -> str:
        return str(self.id)

    
class wishlist(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return  str(self.id)
    
        
class homepage(models.Model):
    Homedescription=models.TextField(blank=True)
    home_anime_name=models.CharField(blank=True, max_length=50)
    homepage_thumbnail=models.URLField(max_length=200)
    def __str__(self):
        return self.home_anime_name
    
class feedback(models.Model):
    feedbck=models.TextField(blank=True)

