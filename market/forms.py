from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('image', 'title', 'price', 'subject',
        'seller', 'description')

# class UserRegistrationForm(forms.Form):
#     email = forms.CharField(
#         required = True,
#         label = 'Email',
#         max_length = 32,
#     )
#     password = forms.CharField(
#         required = True,
#         label = 'Password',
#         max_length = 32,
#         widget = forms.PasswordInput()
#     )

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user