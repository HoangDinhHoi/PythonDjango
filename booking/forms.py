# version django == 2.0.7
from django.forms import ModelForm
from .models import Book
from django import forms
# from bootstrap_datepicker.widgets import DatePicker
# from django.contrib.admin import widgets

# form for booking
class BookForm(ModelForm):
    """docstrings"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "What is your email?"
        self.fields['name'].label = "What is your name?"
        self.fields['date'].label = "What date do you want?"
        self.fields['book_time'].label = "What time do you want?"
        self.fields['menu'].label = "What type do you want?"
        
    class Meta:
        model = Book
        fields = ['name', 'menu', 'date', 'book_time', 'email',] # new in 2.0.7
