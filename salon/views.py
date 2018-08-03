from django.shortcuts import render, HttpResponseRedirect
from pricemenu.models import PriceMenu
from pricemenu.forms import PriceMenuForm
from .forms import RegistrationForm

def home(request):
    template = 'home.html'
    price_menu_list_3 = PriceMenu.objects.all()[:3]
    price_menu_list_remain = PriceMenu.objects.all()[3:]
    new_price_list = [price_menu_list_remain[i: i+3] for i in range(0, len(price_menu_list_remain),3)]
    return render(request, template, locals())

# handle error page 


def handle_errors(request):
    return render(request, 'blog/handle_error.html', locals())

def register(request):
    # to register for user
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'register.html', locals())