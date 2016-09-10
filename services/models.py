# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from core.models import User
from cars.models import Breakdown


class Service(models.Model):
    class Meta:
        verbose_name = u'Автосервис'
        verbose_name_plural = u'Автосервисы'

    owner = models.ForeignKey(User, verbose_name=u'Администратор автосервиса', null=True)
    name = models.CharField(max_length=100, verbose_name=u'Название автосервиса')
    phone = models.CharField(max_length=100, verbose_name=u'Номер телефона')
    address = models.CharField(max_length=250, verbose_name=u'Адрес')
    about = models.TextField(max_length=1000, verbose_name=u'Об автосервисе', blank=True)
    site = models.CharField(max_length=50, verbose_name=u'Сайт', unique=True, blank=True)

    def __unicode__(self):
        return self.name

    def as_dict(self, breakdown_id=None):
        dict = {
            'name': self.name,
            'phone': self.phone,
            'address': self.address,
            'about': self.about,
            'site': self.site
        }
        if breakdown_id:
            dict.update({
                'price': Work.objects.filter(service=self, breakdown_id=breakdown_id).first().price
            })
        return dict


class Work(models.Model):
    class Meta:
        verbose_name = u'Работа-цена'
        verbose_name_plural = u'Работы-цены'

    service = models.ForeignKey(Service, verbose_name=u'Автосервис', null=True)
    breakdown = models.ForeignKey(Breakdown, verbose_name=u'Поломка')
    price = models.PositiveIntegerField(default=0, verbose_name=u'Цена')

    def __unicode__(self):
        return (self.service.name if self.service else '') + ' ' + self.breakdown.name + ' ' + str(self.price)