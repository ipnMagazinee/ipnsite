
from django.urls import path
#  views
from apps.editor.views import *

app_name = 'editor'

urlpatterns = [
    path('<str:name>/', EditorListView.as_view(), name='editor'),
]

