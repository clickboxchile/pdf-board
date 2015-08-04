# -*- coding: utf8 -*-

from django.views import generic
from django.db.models import Q
from empleos.models import Empleo
import forms

from django.shortcuts import get_object_or_404


import xhtml2pdf.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse

from django import http
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context


class EmpleoListView(generic.ListView):
    model = Empleo
    context_object_name = 'empleos_list'
    template_name = 'empleos/index.html'
    paginate_by = 20

    def get_queryset(self):

        results = Empleo.objects.all()

        q = self.request.GET.get('q', None)
        if q:
            results = results.filter(
                Q(titulo__icontains=q) |
                Q(ciudad__nombre__icontains=q) |
                Q(categoria__nombre__icontains=q) |
                Q(descripcion__icontains=q) |
                Q(nombre_empresa__icontains=q) |
                Q(email_empresa__icontains=q))

        return results.order_by('-fecha_creado')

    def get_context_data(self, **kwargs):
        context_data = super(EmpleoListView, self).get_context_data(**kwargs)
        context_data['q'] = self.request.GET.get('q', '')
        return context_data


class EmpleoCreateView(generic.CreateView):
    model = Empleo
    template_name = 'empleos/new.html'
    form_class = forms.EmpleoForm

    def get_success_url(self):
        return reverse('empleos:index')


class EmpleoDetailView(generic.DetailView):
    model = Empleo
    template_name = 'empleos/detail.html'
    context_object_name = 'empleo'


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), content_type='application/pdf')
    return http.HttpResponse('We had some errors<pre>%s</pre>' % cgi.escape(html))

def contrato(request, id):
    model=get_object_or_404(Empleo, id=id)
    return render_to_pdf('contrato.html',{
        'pagesize':'A4',
        'empleo':model})