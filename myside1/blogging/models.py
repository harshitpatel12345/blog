from django.db import models
from froala_editor.fields import FroalaField
from django.contrib.auth.models import  AbstractUser
from django.conf import settings


# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='media')

class Blog(models.Model):
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='blogs')
    title = models.CharField(max_length=100)
    content = FroalaField()
    image = models.ImageField(upload_to='media')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_to = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    


class Comment(models.Model):
    blog = models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.blog.title
    
class Like(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,related_name='likes',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    
class Follow(models.Model):
    author = models.ForeignKey(CustomUser, related_name='following', on_delete=models.CASCADE)
    follower = models.ForeignKey(CustomUser, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('author', 'follower')

    def __str__(self):
        return self.author.username
    
class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    expiry = models.DateField()
    



