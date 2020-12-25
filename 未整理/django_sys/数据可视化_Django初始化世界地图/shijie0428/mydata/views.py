from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def data_demo(request):
    # return HttpResponse("hello")
    return render(request, 'g_推文/shijie.html')


def test(request):
    return HttpResponse("hello")
