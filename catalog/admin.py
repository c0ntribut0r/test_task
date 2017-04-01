from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.html import format_html

from .models import Car, CarPart


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CarPart)
class CarPartAdmin(admin.ModelAdmin):
    list_display = ['number', 'price', 'get_cars']

    def get_cars(self, instance):
        return format_html('<br>'.join([str(car) for car in instance.cars.all()]))
    get_cars.short_description = _('cars')
