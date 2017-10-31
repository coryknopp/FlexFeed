from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^groups/$', views.groups, name='groups'),
    url(r'^login/$', views.login, name='login'),
    url(r'^discovery/$', views.discover, name='discover'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^groups/edit/$', views.editgroups, name='edit')
]
