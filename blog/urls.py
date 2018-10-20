from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listado, name="listado"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detallepost,  name='detallepost'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
