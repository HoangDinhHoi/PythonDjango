from .views import images, delete
from django.conf.urls import url

# Create anything url
urlpatterns = [
    url(r"^images/", images, name="images"),
    url(r'^delete/(?P<id>.*)/$', delete, name="delete_image"),

]
