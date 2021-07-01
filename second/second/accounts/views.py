from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.


def home(request):
    #persons = Person.objects.all()
    persons = Person.objects.filter(is_verify=False)
    context = {'persons': persons}
    return render(request, 'persons.html', context)
