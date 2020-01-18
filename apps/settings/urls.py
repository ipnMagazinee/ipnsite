
from django.urls import path
from apps.settings.views import *

app_name = 'settings'

urlpatterns = [
    path('<str:name>/', SettingsView.as_view(), name='settings'),
]
