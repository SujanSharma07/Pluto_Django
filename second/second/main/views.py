from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignupForm
from django.contrib import messages

# Create your views here.


def home(request):
    return HttpResponse("We are in home of main application")


def create(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "User Saved Successfully")
            form = SignupForm()
        else:
            messages.error(request, "Please Provide valid data")

    #context = {'form': form, 'messages': messages}
    return render(request, 'create_user.html', locals())
