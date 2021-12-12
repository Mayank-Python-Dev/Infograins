from django import forms
from .models import *
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# print(request.user.username)

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = "__all__"
		widgets = {
        'manufacture_date': forms.DateInput(format=('%Y/%m/%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'expiry_date': forms.DateInput(format=('%Y/%m/%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'})
        }

class RegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']