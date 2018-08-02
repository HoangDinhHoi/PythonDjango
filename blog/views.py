"""docstrings"""
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # import de phan trang



# Create your views here.

def add_comment_to_post(request, pk):
    # post = BlogPost.objects.get(pk=pk)
    post = get_object_or_404(BlogPost, pk=pk)
    form = CommentForm()
    comments = Comment.objects.all().order_by("-comment_date")

    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(request.path)
        
    return render(request, 'blog/post.html', locals())

def list(request):
    
    post_list = BlogPost.objects.all().order_by('-timestamp')
    paginator = Paginator(post_list, 3)

    pageNumber = request.GET.get('page') #so thu tu cua trang muon xem

    try:
        posts = paginator.page(pageNumber)
    except PageNotAnInteger:# neu nhu trang yeu cau khong phai la number
        posts = paginator.page(1) #tra ve trang dau tien
    except EmptyPage: #neu nhu trang yeu cau vuot qua so trang hien co
        posts = paginator.page(paginator.num_pages) #tra ve trang cuoi cung
    return render(request, 'blog/list.html', locals())

def handle_errors(request):
    return render(request, 'blog/handle_error.html', locals())
#generic 

# class PostListView(ListView):
#     """docstrings"""
#     queryset = BlogPost.objects.all().order_by('-timestamp')
#     model = BlogPost
#     context_object_name = 'Posts'
#     template_name = 'blog/list.html'
#     paginate_by = 2 #pagination 

class PostDetailView(DetailView):
    """optimize code by generic"""
    model = BlogPost
    template_name = 'blog/post.html'
