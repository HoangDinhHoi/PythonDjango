from django.contrib import admin

# Register your models here.
from .models import BlogPost, Comment

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'timestamp', 'image_post',)
    search_fields = ('title',)
    class Meta:
        model = BlogPost

admin.site.register(BlogPost, BlogPostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('title_comment', 'author', 'post', 'comment_date', 'body',)
    search_fields = ('author',)
    class Meta:
        model = Comment
    
admin.site.register(Comment, CommentAdmin)