# from django.urls import path
from .views import pricetable, edit, delete
from django.conf.urls import url
# create urlpatterns
urlpatterns = [
    url(r"^pricelist/", pricetable, name="pricetable"),
    # url(r"^about/", about, name="about"),
    # url(r"^success/", success, name="success"),
    # url(r"^book_list/", book_list, name="book_list"),
    url(r'^edit/(?P<id>.*)/$', edit, name="edit_price"),
    url(r'^delete/(?P<id>.*)/$', delete, name="delete_price"),
]
