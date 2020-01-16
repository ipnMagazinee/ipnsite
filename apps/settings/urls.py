
from django.urls import path
from apps.settings.views import *

app_name = 'settings'

urlpatterns = [
    path('user/<str:name>', SettingsUserView.as_view(), name='user'),
    path('user/<str:name>', SettingAdminView.as_view(), name='admin'),
]
