from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.conf import settings


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        ordering = ['nombre']

    def __unicode__(self):
        return self.nombre


class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        ordering = ['nombre']

    def __unicode__(self):
        return self.nombre


class Empleo(models.Model):
    titulo = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    categoria = models.ForeignKey(Categoria, default=4)
    ciudad = models.ForeignKey(Ciudad, default=1)
    descripcion = models.TextField()
    forma_contacto = models.TextField()
    nombre_empresa = models.CharField(max_length=50)
    email_empresa = models.EmailField(max_length=50)
    telefono_empresa = models.CharField(max_length=30, default=None, blank=True, null=True)
    url_empresa = models.URLField(max_length=50, default=None, blank=True, null=True)
    fecha_creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_creado']

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        url_partial = reverse('empleos:detail', kwargs={'pk': self.id, 'slug': self.slug})
        url_full = 'http://%s%s' % (settings.DOMAIN_NAME, url_partial)
        return url_full

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Empleo, self).save(*args, **kwargs)