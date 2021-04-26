# ttsx
天天生鲜购物网站

脚手架 python install django==2.2
安装django命令:`pip install django`

安装 `django-admin` 

`django-admin`

生成：
  ```text
你的目录名称
   hello_reg  # 目录
        hello_reg  # 目录
            __init__.py
            asgi.py
            settings.py
            urls.py
            wsgi.py
   helloApp # 目录
        migrations  # 目录 数据迁移包，负责迁移文件和生成文件数据库表数据
            __init__.py # 空文件，指定当前文件目录可以作为包使用
            admin.py # 后台管理工具，后期可以通过该文件管理模型和数据库
            apps.py # Django的生成app名称文件
            models.py # 模型文件，该文件用于存储数据库表的映射
            tests.py # 用于开发测试，在实际开发过程中，诺需要对模块进行测试，可在此文件中编写测试代码
            views.py # 视图文件，在该文件中编写与视图相关的代码
        db.sqlite3
        manage.py
```
  
  创建 app项目名称：
    `python manage.py startapp  名称自定义`
    
 
 ce 进入文件夹目录
  
 使用：`pyhton manage.py startapp  APP名称`
 
 之后多出的目录就是上面注释的目录
 
 在app目录下的views.py 文件下添加方法,
 导入HttpResponse模块
 ```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse("hello world!")
```

在 urls.py 文件下添加路径映射或者叫路由
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello), # 新添加
]

```

之后命令行运行`python manage.py runserver`



创建数据库
`create databases ttsx charset=utf-8`