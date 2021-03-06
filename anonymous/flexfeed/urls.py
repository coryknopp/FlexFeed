from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^groups/$', views.groups, name='groups'),
    url(r'^login/$', views.login, name='login'),
    url(r'^discovery/$', views.discover, name='discover'),
    url(r'^settings/$', views.settings, name='settings')
]

urlpatterns += [
    url(r'^editprofile/', views.edit_Profile, name='editprofile'),
]

# url mapping for viewing specific groups in home page
urlpatterns += [
    url(r'^(?:(?P<pk>[-\w]+))?/$', views.index, name='view_group'),
]

# url mapping for editing, deleting, and adding specific groups
urlpatterns += [
    url(r'^groups/edit_group(?:/(?P<pk>[-\w]+))?/$', views.edit_members, name='edit_group'),
    url(r'^groups/delete/(?:/(?P<pk>[-\w]+))?/$', views.delete, name='delete'),
    url(r'^groups/add/(?:/(?P<pk>[-\w ]+))?/$', views.add, name='add'),
    url(r'^groups/delete-member/(?:/(?P<pk_group>[-\w]+))?/(?:/(?P<pk_member>[-\w]+))?/$', views.delete_member, name='delete-member'),
    url(r'^groups/add-member/(?:/(?P<pk_group>[-\w]+))?/(?:/(?P<member_name>[-\w\s\-]+))?/$', views.add_member, name='add-member'),
    url(r'^queryData', views.getResults , name='queryData'),
]
