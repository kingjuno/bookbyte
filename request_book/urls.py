from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

app_name='request'

urlpatterns = [
    url(r'^create/$',views.request_create,name='request'),
    url(r'^(?P<user>[\w-]+)/(?P<slug>[\w-]+)/$',views.request_detail,name='req_user'),
]
