
from django.urls import path
from apps.administrator.views import *

app_name = 'administrator'

urlpatterns = [
    path('', AdministratorView.as_view(), name='administrator'),
    path('get_username', get_username, name='get_username'),
]
