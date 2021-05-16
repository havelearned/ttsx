from django.db import models


# Create your models here.
# 用户模型
class User(models.Model):
    NO = 1
    OFF = 2
    STATUS_CHOICES = {
        (NO, '正常'),
        (OFF, '锁定')
    }

    class Meta:
        verbose_name_plural = '用户列表'

    user_name = models.CharField(max_length=30, unique=True, verbose_name='用户名称')  # 用户名称
    pwd = models.CharField(max_length=200, verbose_name='用户密码')  # 用户密码
    status = models.IntegerField(verbose_name='状态', choices=STATUS_CHOICES, default=NO)  # 状态
    phone = models.CharField(max_length=100, unique=True, verbose_name='手机号')  # 手机号


# 收货地址
class Adderss(models.Model):
    class Meta:
        verbose_name_plural = '收货地址'

    user = models.ForeignKey("User", on_delete=models.CASCADE)  # 一个收货地址对应一个user
    user_name = models.CharField(max_length=20, unique=True, verbose_name='用户昵称')  # 用户昵称
    phone = models.CharField(max_length=30, unique=True, verbose_name='手机号')  # 手机号
    address = models.CharField(max_length=200, null=False, verbose_name='收货地址')  # 收货地址
    is_default = models.IntegerField(verbose_name='备注')  # 备注

    def __str__(self):
        return f"昵称：{self.user_name}\n手机号:{self.phone}\n收货地址:{self.address}"


# 商品列表
class Goods(models.Model):
    J = '1'
    K = '2'
    L = '3'
    UNIT_CHOICES = {
        (J, '斤'),
        (K, '克'),
        (L, '俩')
    }

    class Meta:
        verbose_name_plural = '商品列表'

    # Type = models.ManyToManyField("Type")  # 与类型表是1对多关系
    good_name = models.CharField(max_length=30, verbose_name='商品名称')  # 商品名称
    img_url = models.ImageField(upload_to='img', verbose_name='商品图片地址')  # 商品图片地址
    price = models.IntegerField(verbose_name='单价')  # 商品 单价格
    intro = models.TextField(verbose_name='介绍')  # 商品 介绍
    unit = models.CharField(max_length=30, default=K, verbose_name='重量', choices=UNIT_CHOICES)  # 重量
    # type_id = models.IntegerField(verbose_name='商品类型')  # 商品类型


# 商品类别
class Type(models.Model):
    class Meta:
        verbose_name_plural = '商品类别'

    # typeId = models.IntegerField(verbose_name="id", auto_created=0)
    type_name = models.CharField(max_length=30, unique=True, verbose_name='商品类别')  # 商品类别

    def __str__(self):
        return self.type_name


# 购物车
class Cart(models.Model):
    class Meta:
        verbose_name_plural = '购物车'

    # user_Cart = models.ForeignKey("User", on_delete=models.CASCADE)  # 一个购物对应一个user
    # good_id = models.IntegerField(verbose_name='商品id')  # 商品id
    unm = models.IntegerField(verbose_name='用户名称')  # 用户名称
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name='用户')  # 用户id
    goods = models.ManyToManyField(Goods)  # 多对多


# 订单表
class Order(models.Model):
    NO = 1
    OFF = 2
    STATUS_CHOICES = {
        (NO, '正常'),
        (OFF, '锁定')
    }

    PAY_STATUS = {
        (NO, '完成'),
        (OFF, '取消')
    }

    class Meta:
        verbose_name_plural = '订单表'

    # orderDetail = models.ForeignKey("OrderDetail", on_delete=models.CASCADE)  # 一个订单有一个订单详情
    # user_Order = models.ForeignKey("user", on_delete=models.CASCADE)  # 一个订单对应一个user
    order_no = models.CharField(max_length=30, unique=True, verbose_name='订单编号')  # 订单编号
    status = models.IntegerField(default=0, verbose_name='订单状态', choices=STATUS_CHOICES)  # 订单状态

    time = models.DateField(auto_now_add=True, verbose_name='时间')  # 时间

    user_name = models.CharField(max_length=20, verbose_name='下单用户昵称')  # 下单用户昵称

    phone = models.CharField(max_length=30, verbose_name='下单用户手机号')  # 下单用户手机号

    address = models.CharField(max_length=200, verbose_name='下单用户地址')  # 下单用户地址
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name='下单用户id')  # 下单用户id
    total_price = models.IntegerField(verbose_name='商品价格')  # 商品价格
    pay_status = models.IntegerField(default=0, verbose_name='是否完成状态', choices=PAY_STATUS)  # 是否完成状态


# 订单详情
class OrderDetail(models.Model):
    class Meta:
        verbose_name_plural = '订单详情'

    # order_OrderDetail = models.ForeignKey("Order", on_delete=models.CASCADE)  # 一个订单详情对应一个订单
    good_name = models.CharField(max_length=30, verbose_name='下单的商品名称')  # 下单的商品名称
    price = models.IntegerField(verbose_name='下单商品的价格')  # 下单商品的价格
    num = models.IntegerField(verbose_name='下单商品的个数')  # 下单商品的个数
    img_url = models.CharField(max_length=100, verbose_name='商品图片')  # 商品图片
    total_price = models.IntegerField(verbose_name='总价格')  # 总价格
    order = models.ForeignKey("Order", on_delete=models.CASCADE, verbose_name='订单id')  # 订单id
