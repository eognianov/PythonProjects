from django.conf.urls import include, url

from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.ContactsList.as_view(), name='list-create-contacts'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.ContactEdit.as_view(), name='edit-contact'),
    url(r'^view/(?P<pk>[0-9]+)/$', views.ContactDetail.as_view(), name='view-contact'),
]