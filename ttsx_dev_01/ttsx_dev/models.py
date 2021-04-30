from django.db import models


# Create your models here.
# 用户模型
class User(models.Model):
    user_name = models.CharField(max_length=100, unique=True)  # 用户名称
    pwd = models.CharField(max_length=100)  # 用户密码
    status = models.IntegerField()  # 状态
    phone = models.CharField(max_length=100, unique=True)  # 手机号


# 购物车
class Cart(models.Model):
    user_Cart = models.ForeignKey("User", on_delete=models.CASCADE)  # 一个购物对应一个user
    unm = models.IntegerField()  # 用户名称
    user_id = models.IntegerField()  # 用户id
    good_id = models.IntegerField()  # 商品id


# 收货地址
class Adderss(models.Model):
    user_Adderss = models.ForeignKey("User", on_delete=models.CASCADE)  # 一个收货地址对应一个user
    user_id = models.IntegerField()  # 用户id
    user_name = models.CharField(max_length=100, unique=True)  # 用户昵称
    phone = models.CharField(max_length=100)  # 手机号
    address = models.CharField(max_length=100, null=False)  # 收货地址
    is_default = models.IntegerField()  # 备注


# 订单表
class Order(models.Model):
    orderDetail = models.ForeignKey("OrderDetail", on_delete=models.CASCADE)  # 一个订单有一个订单详情
    user_Order = models.ForeignKey("user", on_delete=models.CASCADE)  # 一个订单对应一个user
    order_no = models.CharField(max_length=100, unique=True)  # 订单编号
    status = models.IntegerField(default=0)  # 订单状态
    time = models.DateField(auto_now_add=True)  # 时间
    user_name = models.CharField(max_length=100)  # 下单用户昵称
    phone = models.CharField(max_length=100)  # 下单用户手机号
    address = models.CharField(max_length=100)  # 下单用户地址
    user_id = models.IntegerField()  # 下单用户id
    total_price = models.IntegerField()  # 商品价格
    pay_status = models.IntegerField(default=0)  # 是否完成状态


# 订单详情
class OrderDetail(models.Model):
    order_OrderDetail = models.ForeignKey("Order", on_delete=models.CASCADE)  # 一个订单详情对应一个订单
    good_name = models.CharField(max_length=100)  # 下单的商品名称
    price = models.FloatField(max_length=100)  # 下单商品的价格
    num = models.IntegerField()  # 下单商品的个数
    img_url = models.CharField(max_length=100)  # 商品图片
    total_price = models.FloatField(max_length=100)  # 总价格
    order_id = models.IntegerField()  # 订单id


class Goods(models.Model):
    Type = models.ManyToManyField("Type")  # 与类型表是1对多关系
    good_name = models.CharField(max_length=100)  # 商品名称
    img_url = models.ImageField(upload_to='img')  # 商品图片地址
    price = models.FloatField(max_length=100)  # 商品 单价格
    intro = models.CharField(max_length=100)  # 商品 介绍
    unit = models.CharField(max_length=100, default='克')  # 重量
    type_id = models.IntegerField()  # 商品类型


class Type(models.Model):
    type_name = models.CharField(max_length=1000, unique=True)  # 商品类别
