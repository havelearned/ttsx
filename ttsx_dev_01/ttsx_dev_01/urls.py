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

urlpatterns = [ path('admin/', admin.site.urls),
                path('index/',views.toindex),
                path('login/',views.tologin),
                path('register/',views.toregister),
                path('loging/',views.uselogin),
                path('register/useRegister/',views.useRegister),
                path('loging/goodDetail/<int:id>/',views.goodDetail)
                ]+ static(settings.IMG_URL, document_root=settings.IMG_ROOT)
# path('login/', views.login_view),
# path('loginOut/', views.login_out),
# path('register/', views.register_view),
# path('login_view2/', views.login_view2),
#
# path('index/', views.register_view),
# path('goodDetail/<int:id>/', views.login_view2),
# path('/', views.toIndex),
