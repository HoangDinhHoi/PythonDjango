"""salon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, handle_errors, register
from django.contrib.auth.views import login, logout
from django.views.static import serve
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    # Link to admin page
    path('admin/', admin.site.urls),
    # Link to home page
    path('', home, name='home'),
    # Link to lesson page
    path('lesson/', include('lessons.urls')),
    # Link to our salon page
    path('salon/', include('booking.urls')),
    # Link to gallery page
    path('gallery/', include('galleries.urls')),
    # Link to price menu
    path("pricemenu/", include('pricemenu.urls')),
    # Blog
    path("blog/", include('blog.urls')),   
    # Link to login of admin page
    path("login/", login, {'template_name':'login.html'}, name= 'login'),
    # Link to logout of admin page
    path('logout/', logout, {'template_name':'logout.html'}, name = 'logout'),

    # Form to register for user
    path("register/", register, name="register"),

    # For display image
    # url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),    
]
handler400 = 'salon.views.handle_errors'
handler403 = 'salon.views.handle_errors'
handler404 = 'salon.views.handle_errors'
handler500 = 'salon.views.handle_errors'

# settings if debug == True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
