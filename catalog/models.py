from django.db import models
from django.utils.translation import ugettext as _
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse

from utils.decorators import validate_on_save
from djmoney.models.fields import MoneyField


class Car(models.Model):
    name = models.CharField(_('name'), max_length=32, unique=True)

    class Meta:
        verbose_name = _('car')
        verbose_name_plural = _('cars')
        ordering = ['name']

    def __str__(self):
        return self.name


@validate_on_save  # we need this because by default validators are not run on model save (https://docs.djangoproject.com/en/1.10/ref/validators/#how-validators-are-run) so in shell we could possibly save wrong number
class CarPart(models.Model):
    number = models.CharField(_('part number'), max_length=10, unique=True, validators=[RegexValidator(regex=r'^[0-9\-]+$')])
    description = models.TextField(_('description'), blank=True)
    price = MoneyField(_('price'), decimal_places=2, max_digits=8, default_currency='USD')
    cars = models.ManyToManyField(Car, verbose_name=_('vehicles'), related_name='parts')

    class Meta:
        verbose_name = _('part')
        verbose_name_plural = _('parts')
        ordering = ['number']

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse('catalog:part', kwargs={'pk': self.pk})
