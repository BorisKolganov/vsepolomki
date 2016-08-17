# coding=utf-8
from __future__ import unicode_literals

from time import timezone

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, is_active, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_superuser=is_superuser, is_active=is_active,
                           **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, is_active=None, **extra_fields):
        return self._create_user(email, password, False, False, is_active, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'

    email = models.EmailField(unique=True, error_messages={
        'required': u'Обязательное поле',
        'invalid': u'Неверный email',
        'unique': u'Пользователь с такой почтой уже существует',
    })
    first_name = models.CharField(max_length=100, verbose_name=u'Имя')
    last_name = models.CharField(max_length=100, verbose_name=u'Фамилия')
    is_staff = models.BooleanField(default=False, verbose_name=u'Персонал')
    is_active = models.BooleanField(default=False, verbose_name=u'Активирован?')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name=u'Дата регистрации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    object = UserManager()

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name