from django import forms 
from .models import *
  
class HotelForm(forms.ModelForm): 
  
    class Meta: 
        model = Item 
        fields = ['image', 'title', 'price', 'subject', 
        'seller', 'description', 'created_date']