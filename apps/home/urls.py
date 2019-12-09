
from django.urls import path
# views
from apps.home.views import *

app_name = 'home'

urlpatterns = [
    path('<str:name>/', PublisherView.as_view(), name='publisher'),
]
