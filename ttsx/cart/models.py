from django.db import models
from goods.models import GoodsInfo


# Create your models here.

class OrderInfo(models.Model):
    """订单信息模型"""
    status = (
        (1, '代付款'),
        (2, '代付款'),
        (3, '代付款'),
        (4, '代付款'),
    )
    order_id = models.CharField(max_length=100)
    order_addr = models.CharField(max_length=100)
    order_recv = models.CharField(max_length=50)
    order_tele = models.CharField(max_length=11)
    order_fee = models.IntegerField(default=10)
    order_extra = models.CharField(max_length=200)
    order_status = models.integerField(default=1, choices=status)


class OrderGoods(models.Model):
    """订单模型"""
    goods_info = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE)
    # 商品数量
    good_nums = models.IntegerField()
    # 商品所属订单
    good_order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
