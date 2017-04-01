from django.views.generic import TemplateView
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from .models import CarPart


class PartView(TemplateView):
    template_name = 'catalog/part.html'

    def get(self, request, *args, **kwargs):
        self.part = get_object_or_404(CarPart, pk=kwargs['pk'])
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data.update({
            'part': self.part,
        })
        return data
