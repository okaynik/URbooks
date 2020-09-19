from django import forms 
from .models import *
  
class ItemForm(forms.ModelForm):
  
    class Meta:
        model = Item 
        fields = ('image', 'title', 'price', 'subject', 
        'seller', 'description')