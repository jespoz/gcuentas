from django.shortcuts import render
from django.views.generic import TemplateView
from .models import TipoComision, SubtipoComision


class Lista(TemplateView):
    template_name = 'listado.html'

    def get_context_data(self, **kwargs):
        context = super(Lista, self).get_context_data(**kwargs)
        context['tipocomision'] = TipoComision.objects.all()
        context['subtipocomision'] = SubtipoComision.objects.all()
        return context