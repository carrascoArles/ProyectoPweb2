from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import request

# Create your views here.
def myHomeView(request , *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html",{})
