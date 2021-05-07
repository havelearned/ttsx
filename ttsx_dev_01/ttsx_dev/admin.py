from django.contrib import admin
from ttsx_dev import models


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ('user_name', 'pwd', 'status', 'phone')

    # 搜素字段
    search_fields = ['user_name']

    # 过滤字段
    list_filter = ['user_name']


admin.site.register(models.User, UserAdmin)


class CartAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ('user_Cart', 'unm', 'user_id', 'good_id')

    # 搜素字段
    search_fields = ['user_Cart']

    # 过滤字段
    list_filter = ['user_Cart']


admin.site.register(models.Cart, CartAdmin)


class AdderssAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ( 'user_id', 'user_name', 'phone', 'address', 'is_default')

    # 搜素字段
    search_fields = ['user_name']

    # 过滤字段
    list_filter = ['user_name']


admin.site.register(models.Adderss, AdderssAdmin)


class OrderAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = (
         'order_no', 'status', 'time', 'user_name', 'phone', 'address', 'user_id',
        'total_price', 'pay_status')

    # 搜素字段
    search_fields = ['user_name']

    # 过滤字段
    list_filter = ['user_name']


admin.site.register(models.Order, OrderAdmin)


class OrderDetailAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ( 'good_name', 'price', 'num', 'img_url', 'total_price', 'order_id')

    # 搜素字段
    search_fields = ['good_name']

    # 过滤字段
    list_filter = ['good_name']


admin.site.register(models.OrderDetail, OrderDetailAdmin)


class GoodsAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ('good_name', 'img_url', 'price', 'intro', 'unit', 'type_id')

    # 搜素字段
    search_fields = ['good_name']

    # 过滤字段
    list_filter = ['good_name']


admin.site.register(models.Goods, GoodsAdmin)


class TypeAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ('type_name','id')
    # 搜素字段
    search_fields = ['type_name']
    # 过滤字段
    list_filter = ['type_name']


admin.site.register(models.Type, TypeAdmin)
