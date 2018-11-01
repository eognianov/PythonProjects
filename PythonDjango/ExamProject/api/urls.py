from django.conf.urls import url, include
from .accounts import views as user_views
from rest_framework.schemas import get_schema_view #schema view

api_layout = get_schema_view('Personal Organizer |Exam Project| API') #schema view

urlpatterns = [
    url(r'^signup/', user_views.SignUp.as_view(), name='user-signup'),
    url(r'^auth/', include('rest_framework.urls')),
    url(r'^users/', include('api.accounts.urls')),
    url(r'^contacts/', include('api.contacts.urls')),
    url(r'^$', api_layout), #schema view
]
