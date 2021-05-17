from django.contrib import admin
from ttsx_dev import models


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ('user_name', 'pwd', 'status', 'phone')

    # 搜素字段
    search_fields = ['user_name', 'phone', 'status']

    # 过滤字段
    list_filter = ['user_name', 'phone', 'status']


admin.site.register(models.User, UserAdmin)


class CartAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ('unm', 'user')

    # 搜素字段
    search_fields = ['unm', 'user']

    # 过滤字段
    list_filter = ['unm', 'user']


admin.site.register(models.Cart, CartAdmin)


class AdderssAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ('user', 'user_name', 'phone', 'address', 'is_default')

    # 搜素字段
    search_fields = ['user', 'user_name', 'phone', 'address', 'is_default']

    # 过滤字段
    list_filter = ['user', 'user_name', 'phone', 'address', 'is_default']


admin.site.register(models.Adderss, AdderssAdmin)


class OrderAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = (
        'order_no', 'status', 'time', 'user_name', 'address', 'user', 'total_price',
        'pay_status')

    # 搜素字段
    search_fields = ['order_no', 'status', 'time', 'user_name', 'address', 'user', 'total_price',
                     'pay_status']

    # 过滤字段
    list_filter = ['order_no', 'status', 'time', 'user_name', 'address', 'user', 'total_price',
                   'pay_status']


admin.site.register(models.Order, OrderAdmin)


class OrderDetailAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ('good_name', 'price', 'num', 'img_url', 'total_price', 'order')

    # 搜素字段
    search_fields = ['good_name', 'price', 'num', 'img_url', 'total_price', 'order']

    # 过滤字段
    list_filter = ['good_name', 'price', 'num', 'img_url', 'total_price', 'order']


admin.site.register(models.OrderDetail, OrderDetailAdmin)


class GoodsAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ('good_name', 'img_url', 'price', 'intro', 'unit', 'goods_type')

    # 搜素字段
    search_fields = ['good_name', 'img_url', 'price', 'intro', 'unit']

    # 过滤字段
    list_filter = ['good_name', 'img_url', 'price', 'intro', 'unit']


admin.site.register(models.Goods, GoodsAdmin)


class TypeAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ['type_name']
    # 搜素字段
    search_fields = ['type_name']
    # 过滤字段
    list_filter = ['type_name']


admin.site.register(models.Type, TypeAdmin)
