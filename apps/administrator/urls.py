
from django.urls import path
from apps.administrator.views import AdministratorView

app_name = 'administrator'

urlpatterns = [
    path('<str:name>/', AdministratorView.as_view(), name='administrator'),
]
