
from django.urls import path

from apps.account.views import *

app_name = 'account'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('signUp/', SignUpView.as_view(), name='signUp'),
    path('getArea/', get_area, name='get_area'),
    path('getDep/<str:area>/', get_department, name='get_dep'),
    path('signOff/<str:name>/', sign_off, name='signOff'),
]
