from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listado),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detallepost, name='detallepost'),
]
