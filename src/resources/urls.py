from django.conf.urls import url
from django.contrib import admin

from .views import (
    resource_list,
    resource_create,
    resource_detail,
    resource_update,
    resource_delete,
    download
)

urlpatterns = [
    url(r'^$', resource_list, name = 'list'),
    url(r'^create/$',resource_create),
    url(r'^detail/(?P<id>\d+)/$', resource_detail, name ='detail'),
    url(r'^edit/(?P<id>\d+)/$', resource_update, name = 'update'),
    url(r'^delete/(?P<id>\d+)/$', resource_delete),
    url(r'^download/(?P<id>\d+)/$', download, name = 'download'),
]
