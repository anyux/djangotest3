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

