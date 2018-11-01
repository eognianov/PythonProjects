from django.conf.urls import include, url

from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.TaskList.as_view(), name='list-create-tasks'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.TaskEdit.as_view(), name='edit-task'),
    url(r'^view/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view(), name='view-task'),
    url(r'^todo/$', views.ToDoList.as_view(), name='view-todo-list'),
]