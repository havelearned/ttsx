from django.db import models


class GoodsCategory(models.Model):
    """GoodsCategory表"""
    cag_name = models.CharField(max_length=30)  # 分类名称
    cag_css = models.CharField(max_length=20)  # 分类样式
    cag_img = models.ImageField(upload_to='cag')  # 分类图片


# Create your models here.

class GoodsInfo(models.Model):
    """GoodsInfo表"""
    goods_name = models.CharField(max_length=100)  # 商品名称
    goods_price = models.IntegerField(default=0)  # 商品价格
    goods_desc = models.CharField(max_length=0)  # 商品详情
    goods_img = models.ImageField(upload_to='goods')  # 商品图片

    goods_cag = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE)
