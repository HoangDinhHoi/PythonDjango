# from django.urls import path
from .views import about, success, book_list, edit, delete
from django.conf.urls import url
# create urlpatterns
urlpatterns = [
    url(r"^about/", about, name="about"),
    url(r"^success/", success, name="success"),
    url(r"^book_list/", book_list, name="book_list"),
    url(r'^edit/(?P<id>.*)/$', edit, name="edit_booking"),
    url(r'^delete/(?P<id>.*)/$', delete, name="delete_booking"),
]
