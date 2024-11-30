from rest_framework import serializers

from app.models import UserInfo, Addr


class UserInfoSerializer(serializers.ModelSerializer):
    """定义用户序列化器"""

    class Meta:
        model = UserInfo
        # 所有字段
        fields = '__all__'
        # 指定序列化字段
        # fields = ('id','age','pwd')
        # 字段id不参与序列化,注意,此字段值必须为 list or tuple
        # exclude = ('id',)
        # read_only_fields = ("id",)
        # 使用extra_kwargs 去修改指定字段的校验规则(反序列化的校验规则)
        extra_kwargs = {
            'pwd': {
                'required': True,
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    ''
                }
            }
        }

class AddrSerializer(serializers.ModelSerializer):
    """定义地址序列化器"""

    class Meta:
        model = Addr
        fields = '__all__'