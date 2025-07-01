from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken

import uuid
from django.contrib.auth import authenticate
class RegisterSerializers(serializers.ModelSerializer):
    """注册只需要用户名和密码"""
    class Meta:
        model= User
        fields=['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},

        }
    def create(self, validated_data):
        # return User.objects.create_user(**validated_data)
        if 'nick_name' not in validated_data:

            unique_id = uuid.uuid4().hex[12]
            validated_data['nick_name'] = f"hk_{unique_id}"

        username = validated_data['username']
        password = validated_data['password']
        return User.objects.create(username=username,
                            password=make_password(password),
                            nick_name=validated_data['nick_name']
                            )

# class LoginSerializers(serializers.ModelSerializer):
    # token
    # class Meta:
    #     model = User
    #     fields = ['username', 'password', 'nick_name', 'avatar', 'birth_date','signature', 'gender', 'last_login_ip', 'token']
    #     extra_kwargs = {
    #         'id': {'read_only': True},
    #         'password': {'write_only': True},
    #         'token': {"read_only": True}
    #     }
    #
    # def validate(self, attrs):
    #     username = attrs['username']
    #     password = attrs['password']
    #
    #     if username and password:
    #         user = authenticate(username=username,password=password)
    #         if user:
    #             if not user.is_avtive():
    #                 raise serializers.ValidationError("用户已被禁用")
    #             attrs['user'] = user
    #             return attrs
    #         else:
    #             raise serializers.ValidationError("验证失败")
    #     else:
    #         raise serializers.ValidationError('用户名或密码不能为空！')
    #
    # def create(self, validated_data):
    #     user = validated_data['user']
    #     token = RefreshToken.for_user(user)
    #     return {
    #         'username': user.username,
    #         'token': token
    #     }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['username', 'nick_name', 'avatar', 'birth_date','signature', 'gender', 'last_login_ip']