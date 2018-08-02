# from django.conf.urls import url
from django.urls import path
from django.conf.urls import url
from .views import add_comment_to_post, list
urlpatterns = [
    # url(r"$", list, name="list_post"),
    # url(r"^/$", .as_view(), name=""),
    # path("", list, name="list_post"),
    path("", list, name="list_post"),
    # path("<int:id>/", add_comment_to_post, name="detail_post"),
    url(r'^(?P<pk>.*)/', add_comment_to_post, name="detail_post"),
    
]
