from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from ttsx_dev import models
from django.db.models import F
import json
import re


#  超链接跳转  a标签 href= /xxxx   请求就行不要多加/ ，或者加个.html django没有办法解析
# urls.py  path('xxxx/',xxx)  这个玩意就必须在后面加个 /
# 方法 render(requset,'xxxx.html')

# 装饰器
def isSuccess(fun):
    def wrapper(request, *args, **kwargs):
        if request.session['user_name']:
            username = request.session['user_name']
            isExist = models.User.objects.get(user_name=username)
            if isExist:
                print("数据库存在这个", username)

                return fun(request, *args, **kwargs)
        else:
            print("没有登录需要登录")
            return render(request, "login.html")

    return wrapper


def toLogin(request, *args):
    print(args)
    return render(request, "login.html")


@isSuccess
def toindex(request):
    username = request.session['user_name']
    return render(request, "index.html",{"user_name":username})


def toregister(request):
    return render(request, "register.html")
