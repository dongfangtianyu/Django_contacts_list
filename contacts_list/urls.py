from django.conf.urls import patterns, url

from contacts_list import views

ss ='1'
urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^list/$', views.list, name='list'),
    # url(r'^list/page/(?P<page_id>\d+)/$', views.index, name='list'),
    url(r'^id/(?P<contact_id>\d+)/$', views.detail, name='detail'),
    url(r'^id/(?P<contact_id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^id/(?P<contact_id>\d+)/edit_save/$', views.edit_save, name='edit_save'),

)