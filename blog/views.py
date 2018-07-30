"""docstrings"""
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator


# Create your views here.

def add_comment_to_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user,
                           post=post)
        if form.is_valid():
            form.save()

            return redirect(pk)
        
    return render(request, 'blog/detail_post.html', locals())

# def list(request):
#     Posts = BlogPost.objects.all().order_by('-timestamp')
#     p = Paginator(Posts, 1)
#     return render(request, 'blog/post.html', locals())

def handle_errors(request):
    return render(request, 'blog/handle_error.html', locals())
#generic 

class PostListView(ListView):
    """docstrings"""
    queryset = BlogPost.objects.all().order_by('-timestamp')
    model = BlogPost
    context_object_name = 'Posts'
    template_name = 'blog/post.html'
    paginate_by = 2 #pagination 

class PostDetailView(DetailView):
    """optimize code by generic"""
    model = BlogPost
    template_name = 'blog/detail_post.html'
