
from django.urls import path
from apps.direction.views import *

app_name = 'direction'

urlpatterns = [
    path('<str:name>/', DirectionListView.as_view(), name='direction'),
    path('<str:name>/<int:id_publication>', ApprovePublication.as_view(), name='approve_publication'),
]
