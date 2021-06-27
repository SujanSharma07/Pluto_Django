from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    try:
        data = request.GET
        email = data['email']
        password = data['pass']
        print(f'Email {email} and password {password}')

    except:
        pass

    return render(request, 'home.html')


def about(request):
    data = request.GET
    email = data['email']
    password = data['pass']
    print(f'Email {email} and password {password} i am in about')
    return HttpResponse('Welcome to About Page ')


def contact(request):
    return HttpResponse('Welcome to Contact Page ')


def dynamic(request, roll):
    print(roll)
    return HttpResponse(f"Hello {roll}")


def dynamic2(request, roll):
    print(roll)
    return HttpResponse(f"Hello {roll}")
