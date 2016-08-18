from django.contrib import admin

# Register your models here.
from cars.models import CarModel, CarBrand, CarModification, BreakdownType, Breakdown

admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(CarModification)
admin.site.register(BreakdownType)
admin.site.register(Breakdown)
