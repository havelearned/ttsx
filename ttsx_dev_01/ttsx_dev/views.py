from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.


def hello(request):
    return HttpResponse("hello world!")


def index(request):
    return render(request, "index.html", {"hello": "hello"})


def login(request):
    return render(request, 'login.html', {"msg": "登录中"})
