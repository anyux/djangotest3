from django.db import models

# Create your models here.

class UserInfo(models.Model):
    """用户信息模型类"""
    name = models.CharField(max_length=20,verbose_name="用户名称")
    pwd = models.CharField(max_length=20,verbose_name="密码")
    email = models.EmailField(max_length=40,verbose_name="邮箱")
    age = models.IntegerField(default=18,verbose_name="年龄")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "userinfo"
        # 后台显示表名称
        verbose_name = "用户信息"
        # 复数形式也显示为单数
        verbose_name_plural = verbose_name


class Addr(models.Model):
    """地址信息模型类"""
    user = models.ForeignKey('UserInfo',verbose_name="所属用户",on_delete=models.CASCADE)
    mobile = models.CharField(verbose_name="手机号",max_length=18)
    city = models.CharField(verbose_name="城市",max_length=10)
    info = models.CharField(verbose_name="详细地址",max_length=200)

    def __str__(self):
        return self.info

    class Meta:
        db_table = "addr"
        verbose_name = "地址表"
        verbose_name_plural = verbose_name


class ImageModel(models.Model):
    """文件上传"""

    # 用于保存文件
    # file = models.IntegerField()

    # 用于保存图片
    path = models.ImageField()

    def __str__(self):
        return self.path

    class Meta:
        db_table = "Images"
        verbose_name = "图片"
        verbose_name_plural = verbose_name













