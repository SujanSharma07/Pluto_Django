from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    print("Home is triggred")
    try:
        data = request.GET
        maths = int(data['maths'])
        social = int(data['social'])
        total = maths + social
        """ 
        pickle_in = open('first/heart.pickle', 'rb')
        reg = pickle.load(pickle_in)
        input_ = np.array([i for i in range(13)]).reshape(-1, 1)
        print(reg.predict(input_)) """

        percentage = total/2
        context = {'t': total, 'per': percentage,
                   'marks': [("Maths", 34), ("Social", 78), ("Science", 34)]}
        return render(request, 'output.html', context)
    except Exception as e:
        print(e)

    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):

    return render(request, 'contact.html')


def dynamic(request, roll):
    print(roll)
    return HttpResponse(f"Hello {roll}")


def dynamic2(request, roll):
    print(roll)
    return HttpResponse(f"Hello {roll}")
