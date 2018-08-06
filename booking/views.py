from django.shortcuts import render, HttpResponseRedirect
from .forms import BookForm
from django.core.mail import send_mail
from django.template.loader import get_template
from .models import Book
#import Form Price
from pricemenu.forms import PriceMenuForm
#import Model Price 
from pricemenu.models import PriceMenu
# lib to require login 
from django.contrib.auth.decorators import login_required
#for calendar
import calendar
import datetime

# from django.template import *
# Create your views here.
def about(request):
    book_form = BookForm
    template = 'booking/book_form.html'
    # show list price from PriceMenu
    price_menu_list_3 = PriceMenu.objects.all()[:3]
    price_menu_list_remain = PriceMenu.objects.all()[3:]
    new_price_list = [price_menu_list_remain[i: i+3]
                      for i in range(0, len(price_menu_list_remain), 3)]

    # check today
    today = datetime.datetime.today()
    c1 = calendar.Calendar(firstweekday=2)
    # create calendar data
    cal = c1.itermonthdays2(today.year, today.month)

    # get all objects of Price Menu
    all_price = PriceMenu.objects.all()

    # get all objects of Book
    all_book_01 = Book.objects.all()

    # retrieve booking data
    all_book = Book.objects.filter(date__year=today.year, date__month=today.month)
    # check request method of form
    if request.method == 'POST':
        form = BookForm(request.POST or None)
        #if form is_valid
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.save()

            # we will send notification email to customer
            send_mail(
                #title of this mail
                'Thank you for your booking from Beauty Salon',
                #select the template for this mail
                get_template('emails/booking_notification.html').render(
                    #we can give some variable to template
                    context={
                        'customer': new_form.name,
                        'menu': new_form.menu,
                        'book_date': new_form.date, 
                    },
                ),
                #FROM
                'hoanghoibk@gmail.com',
                #TO
                [new_form.email],
                fail_silently= True,
            )

            return HttpResponseRedirect('/salon/success/')
    return render(request, template, locals())

def success(request):
    # views for successful booking
    template = 'booking/success.html'
    return render(request, template, locals())

# Must login to show booking list
@login_required
def book_list(request):
    # views for list book in about page
    # get all book of customer in database then show in private page
    # check today
    today = datetime.datetime.today()
    c1 = calendar.Calendar(firstweekday=2)
    # create calendar data
    cal = c1.itermonthdays2(today.year, today.month)

    # retrieve booking data
    all_book_time = Book.objects.filter(date__year=today.year, date__month=today.month)
    all_book = Book.objects.all().order_by('-date')
    template = 'booking/book_list.html'
    return render(request, template, locals())

@login_required
def edit(request, id):
    # get form of class Book
    book_form = BookForm
    
    template = 'booking/edit_booking.html'
    booking = Book.objects.get(id=id)
    # get all objects of Price
    all_price = PriceMenu.objects.all()
    #check request method
    if request.method == 'POST':
        form = BookForm(request.POST or None, instance=booking)
    
    #check content of request
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.save()
        
        #go to book list page
            return HttpResponseRedirect('/salon/book_list/')


    return render(request, template, locals())

@login_required
def delete(request, id):
    booking = Book.objects.get(id=id)

    #check request method
    if request.method == 'POST':
        # delete this booking use method delete()
        booking.delete()
        
        #go to the book list
        return HttpResponseRedirect('/salon/book_list/')


