# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class Node(models.Model):
    car_model = models.ForeignKey("cars.CarModel", null=True, blank=True, verbose_name=u'Модель машины, на которую завязана нода')
    answer_text = models.CharField(max_length=250, blank=True, verbose_name=u'Текст на кнопке ответа у родительской ноды')
    name = models.CharField(max_length=200, blank=True, verbose_name=u'Название ноды')
    node_text = models.TextField(max_length=1000, blank=True, verbose_name=u'Описание ноды')
    root_nodes = models.ManyToManyField("self", blank=True, symmetrical=False)
    instruction = models.ForeignKey("InstructionStep", null=True, blank=True, verbose_name=u'Первый шаг инструкции')
    root = models.BooleanField(default=False, verbose_name=u'Корневая ли нода')
    breakdowns = models.ManyToManyField("cars.Breakdown", blank=True, verbose_name=u'Список возможных поломог')
    mileage = models.IntegerField(default=0, verbose_name=u'Показывать ноду, если пробег больше')
    low_mileage = models.IntegerField(default=10000000, verbose_name=u'Показывать ноду, если пробег меньше')
    need_select = models.BooleanField(default=False, verbose_name=u'Использовать для ответов в верстке селект')

    def __unicode__(self):
        return self.name + ' ' + self.node_text

    def as_dict(self, mileage=1000000):
        return {
            'id': self.id,
            'answer_text': self.answer_text,
            'name': self.name,
            'node_text': self.node_text,
            'root': self.root,
            'instruction': self.instruction.id if self.instruction else None,
            'mileage': self.mileage,
            'need_select': self.need_select,
            'breakdowns': [breakdown.as_dict() for breakdown in self.breakdowns.all().filter(mileage__lte=mileage)] if self.breakdowns else None
        }


class InstructionStep(models.Model):
    text = models.TextField(max_length=1000, blank=True)
    next_step = models.OneToOneField("self", null=True, blank=True)
    img = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return self.text

    def as_dict(self):
        return {
            'text': self.text,
            'img': self.img.url if self.img else None
        }