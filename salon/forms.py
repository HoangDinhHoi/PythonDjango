"""docstrings for forms"""
from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(forms.Form):
    """docstrings"""
    username = forms.CharField(label='Username', max_length=30)
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password Enter', widget=forms.PasswordInput())    
    password2 = forms.CharField(label='Password Enter again', widget=forms.PasswordInput())

    def clean_password2(self):
        # check password2 and password1
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        # generate Error
        raise forms.ValidationError('Error password. Invalid input password')

    def clean_username(self):
        """Test username"""
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username): # check lower case: \w+
            raise forms.ValidationError('Invalid Username')


        try:
            User.objects.get(username=username)  
        except ObjectDoesNotExist:
            return username
        
        raise forms.ValidationError('Exist username')
    
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])
            

