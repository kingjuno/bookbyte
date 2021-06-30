from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

app_name='books'

urlpatterns = [
    path('',views.book_list,name='list'),
    url(r'^create/$',views.book_create,name='create'),
    url(r'^(?P<user>[\w-]+)/(?P<slug>[\w-]+)/$',views.book_detail,name='detail'),
]
