from django.conf.urls import patterns, url, include
from empleos import views

urlpatterns = patterns('',
                       url(r'^$', views.EmpleoListView.as_view(), name='index'),
                       url(r'^new$', views.EmpleoCreateView.as_view(), name='new'),
                       url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)/$', views.EmpleoDetailView.as_view(), name='detail'),
                       url(r'^(?P<id>\d+)/$', 'empleos.views.contrato', name='contrato'),


					   # url(r'^pdf$', 'empleos.views.pdf', name='pdf'),

					   # url(r'^fdp$', 'empleos.views.fdp', name='fdp'),

					   # url(r'^ctm$', 'empleos.views.ctm', name='fdp'),

                       # url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)/$', 'empleos.views.pdf', name='pdf'),


                       # url(r'^(?P<pk>\d+)/$','empleos.views.pdf', name='pdf'),

)