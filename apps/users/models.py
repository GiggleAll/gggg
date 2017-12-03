# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import AbstractUser
import datetime


# Create your models here.


class UserWrapper(AbstractUser):
    nick_name = models.CharField(max_length=30, verbose_name=u'昵称')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    sex = models.CharField(max_length=5, verbose_name=u'性别', choices=(('male', u'男'), ("female", u'女')),
                           default='male')
    address = models.CharField(max_length=100, verbose_name=u'地址', null=True, blank=True)
    mobile = models.CharField(max_length=11, verbose_name=u'手机')
    image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100)

    class Meta:
        db_table = 'users_wrapper'
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name

    def __unicode__(self):
        return self.username


class EmailCode(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'电子邮箱')
    send_type = models.CharField(choices=(('register', u'注册'), ('forget', u'忘记')), max_length=10)
    send_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'发送时间')

    class Meta:
        db_table = 'email'
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

<<<<<<< HEAD
=======
    def __unicode__(self):
        return self.email

>>>>>>> lianghj

class Banner(models.Model):
    index = models.IntegerField(verbose_name=u'序号')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name=u'图片')
    title = models.CharField(max_length=100, verbose_name=u'标题')
    url = models.URLField(max_length=200, verbose_name=u'链接地址')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'添加时间')

    class Meta:
        db_table = 'Banner'
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

