from django import forms
from .models import Person
from datetime import datetime, date
today = date.today()


class PersonForm(forms.ModelForm):
    #year = forms.CharField()
    documents = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
    photo = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control'}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}))
    age = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your age here'}))
    """ age = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your age here','type':'number'})) """
    dob = forms.DateField(widget=forms.DateTimeInput(
        format=('%Y-%m-%d'), attrs={'class': 'form-control datepicker', 'value': today, 'type': 'date'}), label='जन्म की तारीख')  # ,required=False
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your Email', 'type': 'email'}))
    desc = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter Description'}))
    salary = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form_sal', 'placeholder': 'Enter your Salary'}))

    # gender =
    # citizen =
    # rooms =
    # language =
    # images =

    class Meta:
        model = Person
        fields = "__all__"
        #exclude = ['age','is_verify']
        #fields = ['year', 'first_name', 'last_name']
        widgets = {
            'gender': forms.Select(attrs={'class': 'custom-select'}),
            'citizen': forms.Select(attrs={'class': 'custom-select'}),
            'rooms': forms.Select(attrs={'class': 'custom-select'}),
            'year': forms.Select(attrs={'class': 'custom-select'}),


        }
        labels = {
            'gender': 'लिंग',
        }

        # errors = {
        #     'email':{'required':,'invalid':"Hello all invalid data"}

        # }
