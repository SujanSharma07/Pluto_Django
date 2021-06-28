from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    try:
        data = request.GET
        maths = int(data['maths'])
        social = int(data['social'])
        total = maths + social
        percentage = total/2
        context = {'t': total, 'per': percentage,
                   'marks': [("Maths", 34), ("Social", 78), ("Science", 34)]}
        return render(request, 'output.html', context)
    except:
        pass

    return render(request, 'home.html')


def about(request):
    print("about is called")
    return render(request, 'home.html')


def contact(request):
    return HttpResponse('Welcome to Contact Page ')


def dynamic(request, roll):
    print(roll)
    return HttpResponse(f"Hello {roll}")


def dynamic2(request, roll):
    print(roll)
    return HttpResponse(f"Hello {roll}")
