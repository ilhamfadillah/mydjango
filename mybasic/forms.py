from django import forms
from .models import Person

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = {'first_name', 'last_name'}

    #order fields 
    field_order = ['first_name', 'last_name']