# version django == 2.0.7
from django.forms import ModelForm
from .models import Book
# from bootstrap_datepicker.widgets import DatePicker
# from django.contrib.admin import widgets

# form for booking
class BookForm(ModelForm):
    """docstrings"""
    class Meta:
        model = Book
        fields = ['name', 'menu', 'date', 'book_time', 'email',] # new in 2.0.7