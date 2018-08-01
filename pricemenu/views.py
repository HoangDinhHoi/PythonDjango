from django.shortcuts import render, HttpResponseRedirect
from .models import PriceMenu
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from .forms import PriceMenuForm
# Create your views here.

def pricetable(request):
    all_price = PriceMenu.objects.all().order_by('-pub_date')
    add(request)
    return render(request, 'pricemenu/pricetable.html', locals())

def edit(request, id):
    form_price = PriceMenuForm
    pricelist = PriceMenu.objects.get(id=id)

    # check method POST
    if request.method == "POST":
        form = PriceMenuForm(request.POST or None, request.FILES or None, instance=pricelist)
    
    # check content of request
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.save()

            return HttpResponseRedirect('/pricemenu/pricelist/')
    return render(request, 'pricemenu/editprice.html', locals())

@login_required
def delete(request, id):
    pricelist = PriceMenu.objects.get(id=id)

    if request.method == "POST":
        pricelist.delete()

        return HttpResponseRedirect('/pricemenu/pricelist/')


@login_required
def add(request):
    # check method POST
    if request.method == 'POST':
        form = PriceMenuForm(request.POST or None, request.FILES or None)

        # check content of request
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.save()

            # go to list price table page
            return HttpResponseRedirect('/pricemenu/pricelist/')

