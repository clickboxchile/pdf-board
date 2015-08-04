# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Empleo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=100)),
                ('descripcion', models.TextField()),
                ('forma_contacto', models.TextField()),
                ('nombre_empresa', models.CharField(max_length=50)),
                ('email_empresa', models.EmailField(max_length=50)),
                ('telefono_empresa', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('url_empresa', models.URLField(default=None, max_length=50, null=True, blank=True)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(default=4, to='empleos.Categoria')),
                ('ciudad', models.ForeignKey(default=1, to='empleos.Ciudad')),
            ],
            options={
                'ordering': ['-fecha_creado'],
            },
        ),
    ]
