from django.http import HttpResponse
from django.shortcuts import render
from .models import lugar, place


# Create your views here.

def demo(request):
    obj = lugar.objects.all()
    object = place.objects.all()
    return render(request, 'index.html', {'result': obj, 'results': object})

# def demo(request):
#     object=place.objects.all()
#     return render(request, 'index.html',{'results':object})


# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add = x + y
#     min = x - y
#     mult = x * y
#     div = x / y
#     return render(request, 'result.html',
#                   {'addition': add, 'substraction': min, 'multiplication': mult, 'division': div})
