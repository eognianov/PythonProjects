from django.conf.urls import url, include

urlpatterns = [
    url(r'^articles/', include('api.articles.urls'))
]
