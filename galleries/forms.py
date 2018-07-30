# version django == 2.0.7
from django.forms import ModelForm
from .models import StyleImage
from django import forms

# form for booking


class StyleImageForm(forms.ModelForm):
    class Meta:
        model = StyleImage
        fields = ['title', 'description', 'image', ]  # new in 2.0.7 must have
