"""docstring for models: Have a class is Book Class"""

from django.db import models
from pricemenu.models import PriceMenu
# BOOK_TIME
BOOK_TIME = (
    ('1', '10-12'),
    ('2', '12-14'),
    ('3', '14-16'),
    ('4', '16-20'),
)
# for booking
class Book(models.Model):
    """ docstrings for Book class """
    name = models.CharField(max_length = 50)
    menu = models.ForeignKey(PriceMenu, on_delete=models.SET_NULL, null=True)
    # menu = models.CharField(max_length = 50, choices = MENU_LIST, null = True)
    date = models.DateField(auto_now = False)
    email = models.EmailField(max_length = 75, null = True)
    book_time = models.CharField(max_length = 50, choices = BOOK_TIME, null = True)

    def __str__(self):
        return self.name
