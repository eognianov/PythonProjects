from django.conf.urls import include, url

from django.contrib import admin

from contacts import views

urlpatterns = [
    url(r'^api/', views.contact_list)
]