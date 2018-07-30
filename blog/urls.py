# from django.conf.urls import url
from django.urls import path
from .views import PostListView, add_comment_to_post
urlpatterns = [
    # url(r"$", list, name="list_post"),
    # url(r"^/$", .as_view(), name=""),
    # path("", list, name="list_post"),
    path("", PostListView.as_view(), name="list_post"),
    path("<int:pk>/", add_comment_to_post, name="detail_post"),
]
