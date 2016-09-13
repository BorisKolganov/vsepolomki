# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.db.models import Max, Min
from django.utils import timezone


class CarBrand(models.Model):
    class Meta:
        verbose_name_plural = u'Марки машин'
        verbose_name = u'Марки машины'

    name = models.CharField(max_length=100, verbose_name=u'Название марки')

    def __unicode__(self):
        return self.name


class CarModel(models.Model):
    class Meta:
        verbose_name_plural = u'Модели машиин'
        verbose_name = u'Модель машины'

    name = models.CharField(max_length=100, verbose_name=u'Название модели машины')
    brand = models.ForeignKey('CarBrand', verbose_name=u'Марка машины')

    def __unicode__(self):
        return self.brand.__unicode__() + ' ' + self.name


class CarModification(models.Model):
    class Meta:
        verbose_name_plural = u'Модификации машин'
        verbose_name = u'Модификация машины'

    ENGINE_TYPES = (
        (0, 'gasoline'),
        (1, 'diesel'),
        (2, 'hybrid'),
        (3, 'electric'),
    )

    TRANSMISSION_TYPES = (
        (0, 'MT'),
        (1, 'AT'),
        (2, 'AMT'),
        (3, 'CVT')
    )

    DRIVE_TYPES = (
        (0, 'front'),
        (1, 'rear',),
        (2, 'all')
    )

    YEARS = ((i, i) for i in range(1950, timezone.now().year + 1))

    car_model = models.ForeignKey('CarModel', verbose_name=u'Модель машины')
    engine_type = models.IntegerField(choices=ENGINE_TYPES, default=0, verbose_name=u'Тип двигателя')
    transmission_type = models.IntegerField(choices=TRANSMISSION_TYPES, default=0, verbose_name=u'Тип трансмиссии')
    engine_volume = models.IntegerField(verbose_name=u'Объем двигателя', null=True, blank=True)
    horsepower = models.IntegerField(verbose_name=u'Лошадиные силы', null=True, blank=True)
    drive = models.IntegerField(choices=DRIVE_TYPES, default=0, verbose_name=u'Тип привода')
    year_from = models.IntegerField(choices=YEARS, verbose_name=u'С какого года', null=True)
    year_to = models.IntegerField(choices=YEARS, verbose_name=u'По какой год', null=True)

    def __unicode__(self):
        return self.car_model.__unicode__() + ' ' + self.get_engine_type_display() + ' ' + str(self.engine_volume) + ' ' + self.get_transmission_type_display()


class BreakdownType(models.Model):
    class Meta:
        verbose_name_plural = u'Типы поломок'
        verbose_name = u'Тип поломки'

    name = models.CharField(max_length=100, verbose_name=u'Тип поломки')

    def __unicode__(self):
        return self.name


class Breakdown(models.Model):
    class Meta:
        verbose_name_plural = u'Поломки'
        verbose_name = u'Поломка'

    DIFFICULTIES = (
        (0, u'Легко'),
        (1, u'Средне'),
        (2, u'Сложно')
    )

    breakdown_type = models.ForeignKey('BreakdownType', verbose_name=u'Тип поломки', null=True)
    name = models.CharField(max_length=100, verbose_name=u'Название поломки', blank=True)
    difficulty = models.IntegerField(choices=DIFFICULTIES, default=0, verbose_name=u'Сложность поломки')
    jobs_types = models.TextField(max_length=1000, blank=True, verbose_name=u'Виды работ')
    spares = models.TextField(max_length=250, blank=True, verbose_name=u'Запчасти')
    symptoms = models.TextField(max_length=1000, blank=True, verbose_name=u'Симптомы')
    show_services = models.BooleanField(default=True, verbose_name=u'Показывать автосервисы')

    def __unicode__(self):
        return self.name

    def as_dict(self, price=False, brand_id=None):
        from services.models import Work
        dict = {
            'id': self.id,
            'name': self.name,
            'difficulty': self.get_difficulty_display(),
            'jobs_types': self.jobs_types,
            'spares': self.spares,
            'symptoms': self.symptoms,
            'show_services': self.show_services
        }
        if price:
            min_max_dict = Work.objects.filter(breakdown=self, brand_id=brand_id).aggregate(min=Min('price'), max=Max('price'))
            dict.update({
                'price': str(min_max_dict['min']) + '-' + str(min_max_dict['max'])
            })
        return dict