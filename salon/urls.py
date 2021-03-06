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
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from salon.views import home, handle_errors, register

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
    #Add Django site authentication urls (for login, logout, password management)
    path("accounts/", include('django.contrib.auth.urls')),
    # Form to register for user
    path("register/", register, name="register"),
    # For display image
    url(r"^salonshop/", include(('salonshop.urls', 'salonshop'), namespace='salonshop')),
    url(r"^cart/", include(('cart.urls', 'cart'), namespace='cart')),
    url(r"^orders/", include(('orders.urls', 'orders'), namespace='orders')),

]
# settings if debug == True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
