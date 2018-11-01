from django.conf.urls import include, url

from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.MeetingList.as_view(), name='list-create-meeting'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.MeetingEdit.as_view(), name='edit-meeting'),
    url(r'^view/(?P<pk>[0-9]+)/$', views.MeetingDetail.as_view(), name='view-meeting'),
    url(r'^today/$', views.TodayList.as_view(), name='view-today-list'),
]