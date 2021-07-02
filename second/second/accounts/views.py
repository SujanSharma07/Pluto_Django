from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.


def home(request, status):
    if status == "True":
        status = 1
    else:
        status = 0
    #persons = Person.objects.all()
    persons = Person.objects.filter(is_verify=status)

    context = {'persons': persons}
    return render(request, 'persons.html', context)


def person_filter(request):
    try:
        data = request.GET['filter']
        # persons = Person.objects.filter(gender=data).order_by('-id')
        persons = Person.objects.filter(gender=data)
        if data == 'All':
            persons = Person.objects.all()

    except:
        persons = Person.objects.all()

    context = {'persons': persons}
    return render(request, 'persons.html', context)


def create_person(request):

    return render(request, 'create.html')


""" 
Person.objects.create(year="Junior",
                      first_name='rohit',
                      last_name="dubey",
                      age=74,
                      email="rohitpandey@hotmail.com",
                      desc='Random',
                      salary=10000,
                      is_verify=True,
                      prediction =Your_PREDICTED_VALUE) 
"""

"""                     
# Method1
Person.objects.create(year="Junior",
                      first_name='rohit',
                      last_name="dubey",
                      age=74,
                      email="rohitpandey@hotmail.com",
                      desc='Random',
                      salary=10000,
                      is_verify=True)

# Method 2
p1 = Person(year="Junior",
            first_name='shiv shakti',
            last_name="dubey",
            age=74,
            email="ajsdjasbd@hotmail.com",
            desc='Random',
            salary=10000,
            is_verify=True)
p1.save()
"""
