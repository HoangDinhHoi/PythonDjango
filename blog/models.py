from django.db import models
from django.conf import settings
# from .managers import Manager
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    image_post = models.ImageField(upload_to='image_post/', null=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    title_comment = models.CharField(max_length=100, null=True)
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
    
    
