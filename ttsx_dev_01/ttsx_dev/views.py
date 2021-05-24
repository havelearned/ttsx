from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from ttsx_dev import models
import json
import re

# 登录退出
def loginOut(request):
    #清除所有的session
    request.session.flush()
    #重定向到index请求
    return  HttpResponseRedirect("/login")

def check_login(func):
    def warpper(request, *args, **kwargs):
        is_login = request.session.get("is_login", False)
        if is_login:
            print(is_login)
            return func(request, *args, **kwargs)
        else:
            print(is_login)
            return HttpResponseRedirect("/loging")

    return warpper


@check_login
def to_cart(request):
    if request.method == "POST":
        user_name = request.session['user_name']
    if request.method == "GET":
        print("==========to_cart============")
        user_name = request.session['user_name']

        print(user_name)
        return render(request, "cart.html")


def goodDetail(request, id):
    good_detail = models.Goods.objects.get(id=id)
    return render(request, 'detail.html', {'user_name': request.session.get('user_name', None), 'good_detail': good_detail})


#
#
# # Create your views here.
#
# # 首页
# def goodDetail(request, id):
#     good_Detail = models.Goods.objects.get(id=id)
#     return render(request, 'detail.html', {"good": good_Detail, 'user_name': request.session.get('user_name', None)})
#
# # 商品页面
# def index_view(reqeust):
#     goods_list = models.Goods.objects.all()
#     return render(reqeust, 'index.html',
#                   {"goods_list": goods_list, "user_name": reqeust.session.get('user_name', None)})
#
#
# def login_view2(request):
#     if request.method == 'POST':
#         print("hello")
#         user = models.User.objects.all()
#         print(user)
#         return HttpResponse(user)
#     else:
#         print("get")
#         user = models.User.objects.all()
#         print(user)
#         return HttpResponse(user)
#
#
# def login_view(request):
#     if request.method == 'POST':  # 请求是否是 POSt
#         user_name = request.POST.get('user_name', '')  # 获取请求参数
#         pass_word = request.POST.get('pwd', '')
#         user = models.User.objects.get(user_name=user_name, pwd=pass_word)  # 校对数据库
#         if user:  # 返回有数据
#             if pass_word == user.pwd:
#                 request.session['IS_LOGIN'] = True
#                 request.session['user_name'] = user_name
#                 request.session['user_id'] = user.id
#                 return render(request, 'index.html', {'user_name': user_name})  # 转发到首页
#             else:
#                 return render(request, 'index.html', {'error': '用户名或密码错误'})  #
#
#         else:  # 返回无数据
#             return render(request, 'index.html', {'error': '不存在'})
#
#
# def login_out(request):
#     request.session.flush()  # 退出清除本次回话
#     return render(request, 'login.html')
#
#
# def register_view(request):
#     if request.method == 'GET':  # 请求是否是 POSt
#         # return render(request, 'register.html')
#         return render(request, 'login.html')
#     elif request.method == 'POST':
#         user_name = request.POST.get('user_name', '')  # 获取请求参数
#         pass_word_1 = request.POST.get('pwd', '')
#         pass_word_2 = request.POST.get('cpwd', '')
#         phone = request.POST.get('phone', '')
#         if models.User.objects.filter(user_name=user_name):
#             # return render(request, 'register.html', {'error': '用户名已经存在'})
#             return render(request, 'login.html')
#
#         if pass_word_1 != pass_word_2:  #
#             # return render(request, 'register.html', {'error': '两次密码输入不一致'})
#             return render(request, 'login.html')
#         user = models.User()
#         user.user_name = user_name
#         user.pwd = pass_word_1
#         user.phone = phone
#         user.save()
#         # return render(request, 'login.html')
#         return render(request, 'login.html')
#
#     else:  # 返回无数据
#         return render(request, 'register.html')
#         # return render(request, 'login.html')

def useRegister(request):
    user_name = request.POST.get('user_name')
    pwd = request.POST.get('pwd')
    cpwd = request.POST.get('cpwd')
    phone = request.POST.get('phone')
    allow = request.POST.get('allow')

    # 用户名需要中文
    result_name = re.compile(r"[\u4e00-\u9fa5]")
    # 密码只能大小写和数字
    result_password = re.compile(r"^[a-zA-Z]\w{6,18}")
    # 手机只能是11位数
    result_phone = re.compile(r"^1[3578]\d{9}$")
    if not (result_name.match(user_name)):
        return render(request, "register.html", {"nameError": "用户名只能是中文"})
    if pwd == cpwd and result_password.match(pwd):
        return render(request, "register.html", {"passwordErroe": "两次输入的密码错误"})
    if not (result_phone.match(phone)):
        return render(request, "register.html", {"phoneError": "不正确的手机号"})

    if allow == 'on':
        if (models.User.objects.filter(user_name=user_name).exists()) or (
                models.User.objects.filter(phone=phone).exists()):
            return render(request, "register.html", {"nameError": "用户名已经存在", 'phoneError': '手机号已经存在'})
        else:
            user = models.User(user_name=user_name, pwd=pwd, status=1, phone=phone)
            user.save()
    else:
        return render(request, "register.html", {"allowError": "您不必须同意使用条款"})

    return render(request, "login.html", {"loginName": user_name})


def toindex(request):
    type = models.Type.objects.all()
    goods = models.Goods.objects.filter(goods_type_id=1)
    return render(request, 'index.html', {'type_list': type, 'goods_list': goods}, )


def tologin(request):
    return render(request, 'login.html')


def toregister(request):
    return render(request, 'register.html')


def uselogin(request):
    user_name = request.POST.get('user_name')
    pwd = request.POST.get('pwd')
    checkPwd = request.POST.get('checkPwd')

    if request.session.get("is_login") == 1 and user_name == request.session.get('user_name'):
        type = models.Type.objects.all()
        goods = models.Goods.objects.filter(goods_type_id=1)
        # 登录过直接去首页
        return render(request, 'index.html', {'user_name': user_name,
                                              'type_list': type,
                                              'goods_list': goods
                                              },

                      )

    if (models.User.objects.filter(user_name=user_name).exists()) and (models.User.objects.filter(pwd=pwd).exists()):
        if checkPwd == 'on':
            request.session['is_login'] = 1
            request.session['user_name'] = user_name
            request.session.set_expiry(60 * 60 * 24 * 3)
            type = models.Type.objects.all()

        return render(request, 'index.html', {'user_name': user_name, 'type': type})
    else:
        return render(request, 'login.html', {'msg': '用户名或者密码错误'})


def add_cart(request):
    if request.method == "POST":
        pass
    if request.method == "GET":
        good_id = request.GET.get("good_id")
        print(good_id)
    return HttpResponseRedirect('/to_cart')

# 注意事项：
# 1. redirect 是重定向 给出URL路径即可跳转到对应的界面
# 2. render 的第一个参数必须式request ，第二个参数是 渲染的页面， 第三个参数是： map集合
# 3. from 请求表达action属性值必须是login/ 结尾，没有斜杠结尾会报错
# 4. 获取表单参数可以有：request.POST[xxx] 这样做出错率相当的高,如果没有这个参数那么直接报错，
#       request.POST.get(); 这样做可以避免报错，即使没有这个参数会自动赋值为：null
