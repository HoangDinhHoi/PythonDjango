# version django == 2.0.7
from django.forms import ModelForm
from .models import PriceMenu
# from bootstrap_datepicker.widgets import DatePicker
# from django.contrib.admin import widgets

# form for booking


class PriceMenuForm(ModelForm):
    class Meta:
        model = PriceMenu
        fields = ['name', 'price', 'pricemenu_image', ]  # new in 2.0.7
    
