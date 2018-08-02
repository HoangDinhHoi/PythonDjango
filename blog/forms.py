# from django.forms import ModelForm
from django import forms
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    """docstrings"""
    class Meta:
        model = BlogPost
        fields = ["title", "body", "image_post",]

class CommentForm(forms.ModelForm):
    """docstrings"""
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)
        
    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()
    
    class Meta:
        model = Comment
        fields = ['title_comment', 'body',]
