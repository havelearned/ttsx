# ttsx
天天生鲜购物网站
安装 django-admin 脚手架
python install django==2.2
django-admin

生成：
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
  
  创建 app项目名称：
    python manage.py startapp  名称自定义
    
 
  


创建数据库
```sql
create databases ttsx charset=utf-8

```