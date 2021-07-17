from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import PersonForm
from pathlib import Path
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
import os
# Create your views here.


def signout(request):
    request.session.flush()
    logout(request)
    return redirect('accounts:signin')


def signin(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['pass']
        # User.objects.filter(username=username,password=password)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome, {username}")
            if user.is_student:
                return redirect("accounts:pfilter")
            else:
                return redirect("accounts:signin")
        else:
            messages.error(request, 'Please Provide Valid Username / Password')
    if request.user.is_authenticated:
        return redirect('accounts:pfilter')
    return render(request, 'login.html')


def home(request, status):
    if status == "True":
        status = 1
    else:
        status = 0
    #persons = Person.objects.all()
    persons = Person.objects.filter(is_verify=status)

    context = {'persons': persons}
    return render(request, 'persons.html', context)


# @user_passes_test(lambda u: u.is_verified)
@user_passes_test(lambda u: u.is_teacher)
def person_filter(request):
    print('USer is ', request.user.email)
    try:
        data = request.GET['filter']
        # persons = Person.objects.filter(gender=data).order_by('-id')
        persons = Person.objects.filter(gender=data)
        if data == 'All':
            persons = Person.objects.all()

    except:
        data = "All"
        persons = Person.objects.all()

    context = {'persons': persons, 'filter': data}
    return render(request, 'persons.html', context)


def create_person(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.citizen = Citizenship.objects.all().first()
            form.save()
            messages.success(request, "Object Saved Successfully")
            form = PersonForm()
        else:
            messages.error(request, "Please Provide valid data")

    #context = {'form': form, 'messages': messages}
    return render(request, 'create.html', locals())


def edit_person(request, id):
    object_ = Person.objects.filter(id=id).first()
    form = PersonForm(instance=object_)
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES,
                          instance=object_)
        if form.is_valid():
            form.save()
            messages.success(request, "Object Updated Successfully")
            return redirect('pfilter')
        else:
            messages.error(request, "Please Provide valid data")

    return render(request, 'create.html', locals())


def profile(request, id):
    object = Person.objects.filter(id=id)[0]
    return render(request, 'profile.html', locals())


def delete(request, id):
    Person.objects.filter(id=id).first().delete()
    return redirect('accounts:pfilter')


# def create_person(request):
#     if request.method == 'POST':
#         if Person.objects.filter(email=request.POST['email']).count():
#             print("You can not create account with this email")
#         else:
#             Person.objects.create(year=request.POST['year'],
#                                   first_name=request.POST['first_name'],
#                                   last_name=request.POST['last_name'],
#                                   age=request.POST['age'],
#                                   email=request.POST['email'],
#                                   desc=request.POST['desc'],
#                                   salary=request.POST['salary'],
#                                   )
#             print('Object Created Successfully')
#     else:
#         print('GET REQUEST render page only')
#     return render(request, 'create.html')
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
