# coding=utf8
# -*- coding: utf8 -*-

from django import forms
from . import models
from util.email import enviar_correo
from django.template import Context
from django.conf import settings


class EmpleoForm(forms.ModelForm):

    class Meta:
        model = models.Empleo
        fields = ('titulo', 'categoria', 'ciudad', 'descripcion', 'forma_contacto',
                  'nombre_empresa', 'email_empresa', 'telefono_empresa', 'url_empresa')
        labels = {
            'titulo': 'Título del empleo',
            'categoria': 'Categoría',
            'ciudad': 'Ciudad',
            'descripcion': 'Descripción del empleo',
            'forma_contacto': 'Cómo se postularán los candidatos?',
            'nombre_empresa': 'Empresa',
            'email_empresa': 'Email',
            'telefono_empresa': 'Teléfono (Opcional)',
            'url_empresa': 'Sitio Web (Opcional)'
        }
        help_texts = {
            'titulo': 'Ejemplo: “Diseñador Web” o “Programador Android”',
            'descripcion': 'Perfil del candidato. Conocimientos y habilidades requeridas.',
            'forma_contacto': 'Ejemplo: Enviar CV a info@empresa.com o Llamar al 021 333 444 en horario de oficina.',
            'nombre_empresa': 'Ingrese el nombre de la empresa.',
            'email_empresa': 'Dirección a donde se enviará el email de confirmación.',
            'telefono_empresa': 'Ejemplo: +595 021 221 123 o 0981 333 555',
            'url_empresa': 'Ejemplo: http://www.google.com'
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.RadioSelect(attrs={'data-toggle': 'radio'}),
            'ciudad': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'forma_contacto': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'email_empresa': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'url_empresa': forms.URLInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        empleo = super(EmpleoForm, self).save(commit=False)

        if commit:
            empleo.save()

            txt_template = 'empleos/email-confirmacion.txt'
            html_template = 'empleos/email-confirmacion.html'
            data_context = Context({'empleo': empleo})
            asunto, remitente, destinatario =\
                'Publicación de Empleo', settings.EMAIL_HOST_USER, empleo.email_empresa
            enviar_correo(txt_template, html_template, data_context, asunto, remitente, destinatario)

            # Send a copy to the Administrator
            txt_template = 'empleos/alerta-nueva-publicacion.txt'
            html_template = 'empleos/alerta-nueva-publicacion.html'
            data_context = Context({'empleo': empleo})
            asunto, remitente, destinatario =\
                'Nueva Oferta de Empleo', settings.EMAIL_HOST_USER, settings.EMAIL_ADMINISTATOR
            enviar_correo(txt_template, html_template, data_context, asunto, remitente, destinatario)

        return empleo
