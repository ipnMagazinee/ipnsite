
from django.urls import path
# views
from apps.home.views import *

app_name = 'home'

urlpatterns = [
    path('<str:name>/', PublisherView.as_view(), name='publisher'),
    path('get_new_publication', get_new_publication, name='get_new_publication'),  # get template
    path('set_new_publication', set_new_publication, name='set_new_publication'),
]
