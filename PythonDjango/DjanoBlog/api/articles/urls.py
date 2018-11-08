from django.conf.urls import url
from .views import article


urlpatterns=[
    url(r'^$', article, name='articles'),
]