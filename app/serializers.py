from rest_framework import serializers

from app.models import UserInfo, Addr, ImageModel


# def length_validate(value):
#     if not(10<len(value)<20):
#         # 检验未通过,返回错误提示
#         raise serializers.ValidationError("字段的长度不在10和20之间")

class UserInfoSerializer(serializers.ModelSerializer):
    """定义用户序列化器"""
    #指定字段校验,指定检查函数
    # pwd = serializers.CharField(validators=[length_validate])
    class Meta:
        model = UserInfo
        # 所有字段
        fields = '__all__'
        # 指定序列化字段
        # fields = ('id','age','pwd')
        # 字段id不参与序列化,注意,此字段值必须为 list or tuple
        # exclude = ('id',)
        read_only_fields = ("id",)
        # 使用extra_kwargs 去修改指定字段的校验规则(反序列化的校验规则)
        # extra_kwargs = {
        #     'pwd': {
        #         'required': True,
        #         'min_length': 10,
        #         'max_length': 20,
        #     }
        # }
    # 在定义validate_pwd方法后,可以不对序列化的字段指定字段方法,默认可以调用validate_pwd检查此字段信息
    # 同时使用length_validate,extra_kwargs时,先校验length_validate,再extra_kwargs,最后校验validate_pwd方法
    # def validate_pwd(self,value):
    #     """校验逻辑"""
    #     if not (10<len(value)<20):
    #         # 检验未通过,返回错误提示
    #         raise serializers.ValidationError("字段的长度不在10和20之间")



class AddrSerializer(serializers.ModelSerializer):
    """定义地址序列化器"""

    class Meta:
        model = Addr
        fields = '__all__'
        read_only_fields = ("id",)


class ImageSerializer(serializers.ModelSerializer):
    """图片管理序列化器"""

    class Meta:
        model = ImageModel
        fields = '__all__'