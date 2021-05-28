from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from ttsx_dev import models
from django.db.models import F
import json
import re


#  超链接跳转  a标签 href= /xxxx   请求就行不要多加/ ，或者加个.html django没有办法解析
# urls.py  path('xxxx/',xxx)  这个玩意就必须在后面加个 /
# 方法 render(requset,'xxxx.html')

def toLogin(request,*args):
    print(args)
    return render(request, "login.html")


def toindex(request):
    return render(request, "index.html")


def toregister(request):
    return render(request, "register.html")
