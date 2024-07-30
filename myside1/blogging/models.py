from django.db import models
from froala_editor.fields import FroalaField
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blogs')
    title = models.CharField(max_length=100)
    content = FroalaField()
    image = models.ImageField(upload_to='media')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_to = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    


class Comment(models.Model):
    blog = models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.blog.title
    
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,related_name='likes',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    
class Follow(models.Model):
    author = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('author', 'follower')

    def __str__(self):
        return self.author.username
