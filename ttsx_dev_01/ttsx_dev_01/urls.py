"""ttsx_dev_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ttsx_dev import views
from django.conf.urls.static import static
from django.conf import settings
from ttsx_dev.dao import Router

from ttsx_dev.dao import UserDao

# path('admin/', admin.site.urls),
#                path('index/', views.toindex),
#                path('login/', views.tologin),
#                path('register/', views.toregister),
#                # path('loging/', views.uselogin),
#                path('register/useRegister/', views.useRegister),
#                path('goodDetail/<int:id>/', views.goodDetail),
#                path('to_cart/', views.to_cart),
#                path('add_cart/', views.add_cart),
#                path('loginOut/', views.loginOut),
#                path('', views.toindex),
urlpatterns = [
                  # 测试内容与实际项目无关
                  path('userId/<int:id>/', UserDao.queryUserById),
                  path('userLogin/', UserDao.userLogin),  # 用户 登录

                  # 超连接路由
                  path('', Router.toindex),
                  path('index/', Router.toindex),
                  path('login/', Router.toLogin),
                  path('register/', Router.toregister),

              ] + static(settings.IMG_URL, document_root=settings.IMG_ROOT)
# path('login/', views.login_view),
# path('loginOut/', views.login_out),
# path('register/', views.register_view),
# path('login_view2/', views.login_view2),
#
# path('index/', views.register_view),
# path('goodDetail/<int:id>/', views.login_view2),
# path('/', views.toIndex),
