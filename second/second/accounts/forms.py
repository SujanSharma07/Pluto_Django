from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        #exclude = ['age','is_verify']
        #fields = ['year', 'first_name', 'last_name']
