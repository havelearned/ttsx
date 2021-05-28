from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from ttsx_dev import models
from django.db.models import F
import json
import re


# 根据id查询 user对象
def queryUserById(request, id):
    user = models.User.objects.get(id=id)
    user2 = models.User.objects.filter(id=id)
    for item in user2:
        print(item.id)
    return HttpResponse(user2)


# 用户登录处理方法
def userLogin(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        checkMe = request.POST.get('checkPwd')
        print(f"----------用户登录方法UserDao.userLogin:\n用户名：\t{user_name}\n密码：\t{pwd}\n本次是否记住账号：\t{checkMe}\n---------")
        if models.User.objects.filter(user_name=user_name, pwd=pwd):
            request.session['user_name'] = user_name
            if checkMe == "on":
                request.session['pwd'] = pwd
                return HttpResponseRedirect('/index')
        else:
            return HttpResponseRedirect("/login","账号密码错误")
    else:
        return HttpResponseRedirect("/login","请求异常")


# 用户注册处理方法


# 浏览器缓存信息
def geBrowsertSession(request):
    sessions = request.session.items()
    for item in sessions:
        print("session[", item, "]:", item.vales)
    return item
