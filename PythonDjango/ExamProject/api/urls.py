from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

from .accounts import views as user_views
from rest_framework.schemas import get_schema_view

api_layout = get_schema_view('Office staff Organizer |Exam Project| API')
swagger_schema_view = get_swagger_view(title='Office staff Organizer |Exam Project| API')

urlpatterns = [
    url(r'^signup/', user_views.SignUp.as_view(), name='user-signup'),
    url(r'^auth/', include('rest_framework.urls')),
    url(r'^users/', include('api.accounts.urls')),
    url(r'^contacts/', include('api.contacts.urls')),
    url(r'^tasks/', include('api.tasks.urls')),
    url(r'^meetings/', include('api.meetings.urls')),
    url(r'^$', api_layout),
    url(r'^swagger/$', swagger_schema_view),
]
