# ttsx
天天生鲜购物网站

## 安装Django框架

脚手架 python install django==2.2
安装django命令:`pip install django`

`django-admin  startproject my-project` 创建项目 my-project 

`django-admin` 是一个脚手架，使用这个自动生成文件目录结构，

生成：
  ```text
你的目录名称
   my-project  # 目录
        hello_reg  # 目录
            __init__.py
            asgi.py
            settings.py
            urls.py
            wsgi.py
  
  ```

###   创建 app项目名称：

​    `python manage.py startapp  名称自定义`

根目录下多个下面的目录：

```text
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

​    

 cd 进入文件夹目录

 使用：`pyhton manage.py startapp  APP名称`

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



`shop/_init_.py` 文件 引用于类库

导入mysql类库

```python
import pymysql
pymysql.install_as_MySQLdb()
```



### settings.py文件 配置数据源

```python
DATABASES={
	'default':{
		'ENGINE': 'django.db.backends.mysql', # 链接url
        'NAME':'ttsx',  # 数据库名称
        'USER':'root',  # 登录名称
        'PASSWORD':'mysql2020',  # 登录密码
        'HOST':'localhost',  # IP地址
        'PORT':'3306',  # 端口号
	}
}
```





models.py 是编写模型实体类，一张表对应一个模型

所有models 都继承 `models.Model`

```python
class className(models.Model): 
    字段 = model.CharField(max_length=30,null = False)
    字段 = model.IntegerField(max_length=30,unique=True)
    字段 = model.ForeignKey("类名")
    字段 = model.ImageField(upload_to='img')
    
    
    
```

`model.CharField` 对应数据库中的 `varchar`数据类型 ,`max_length=30 `对应`varcahr(30)` 长度

`IntegerField`  对应数据库中的 `int`数据类型 ,`max_length=30 `对应`int(30)` 长度

`model.ForeignKey（“类名”）` 外键关联  一对多

`models.MantoManField`("Type") 多对多





文件迁移，定义完模型之后需要对模型类进行迁移，迁移的目的是通过Django的ORM系统将定义的模型类字段转换为对应的sql语句

使用命令：`python manage.py makemigrations` 生成sql配置文件

使用命令:`python manage.py sqlmigrate AppName 0001` 查看SQL语句

`python manage.py migrate ` 执行SQL，执行文件APPName\ttsx_dev\migrations\0001_initial.py 



最后查看数据库



### 设置 项目后台账号和密码

```bash
E:\Python\ttsx\ttsx_dev_01>python manage.py createsuperuser
Username (leave blank to use 'administrator'): admin
Email address: 1918652173@qq.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: Y
Superuser created successfully.

```



启动项目： python manage.py runserver

浏览器访问：http://127.0.0.1:8000/admin/





添加模板文件 、静态资源

在根目录下创建 templates目录；



修改settings.py文件，添加templates路径

```python
TEMPLATES = [
    {
        ....
        'DIRS': ['DIRS': [os.path.join(BASE_DIR), 'template'],],
			....
            ],
        },
    },
]

....
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

注意入os模块

> 'DIRS': ['DIRS': [os.path.join(BASE_DIR), 'template'],],  让Django认识template目录
>
>  os.path.join(BASE_DIR, 'static') 识别可导入静态资源





