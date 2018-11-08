from django.conf.urls import url, include
from rest_framework import routers
from .authors.views import AuthorViewSet


router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)

urlpatterns =[
    url(r'users/', include('api.users.urls')),
]

#urlpatterns += router.routes
