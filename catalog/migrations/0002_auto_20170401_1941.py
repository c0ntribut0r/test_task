# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 19:41
from __future__ import unicode_literals

from django.db import migrations


def create_cars(apps, schema_editor):
    from catalog.models import Car
    Car.objects.bulk_create([Car(name=name) for name in 'Audi A4, Audi A3, Audi 53, Audi Q5'.split(', ')])


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_cars),
    ]