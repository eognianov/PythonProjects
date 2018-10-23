from django.conf.urls import url
from . import views as user_views


urlpatterns =[
    url(r'^register/$', user_views.SignUpView.as_view(), name='user-signup'),
    url(r'^login/$', user_views.LoginView.as_view(), name='user-login')
]
