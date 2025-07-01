from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    GENDER_CHOICES = (('M', '男'),
                      ('F', '女'),
                      ("U", '保密'))

    nick_name = models.CharField(max_length=40, unique=True, verbose_name="昵称")
    avatar = models.ImageField(upload_to="avatar", verbose_name="头像")
    birth_date = models.DateField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="U", verbose_name="性别")
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)

    class Meta:
        db_table = "dv_user"
        verbose_name = "用户"
        verbose_name_plural = "用户"
