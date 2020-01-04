
from django.urls import path
#  views
from apps.editor.views import *

app_name = 'editor'

urlpatterns = [
    path('<str:name>/', EditorListView.as_view(), name='editor'),
    path('<str:name>/<int:id_publication>/', ReviewPublication.as_view(), name='review'),
]

