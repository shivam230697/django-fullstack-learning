from django import forms
from .models import Person, NewUser, CustomerEntry
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class UserSignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class CustomerEntryForm(forms.ModelForm):
    class Meta:
        model = CustomerEntry
        fields = "__all__"
