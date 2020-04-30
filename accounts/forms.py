from django.forms import ModelForm
from .models import order
from .models import customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms

class OrderForm(ModelForm): #use always camale case
	class Meta:
		model = order
		fields = '__all__'


class CustomerForm(ModelForm):
	class Meta:
		model = customer
		fields = '__all__'


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username' , 'email' , 'password1' , 'password2' ]
		
