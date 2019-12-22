from django.urls import path
# views
from apps.user.views import *

app_name = 'user'

urlpatterns = [
    path('<str:name>/', UserView.as_view(), name='user'),
    path('new_publication/<str:name>', NewPublicationView.as_view(), name='new_publication'),
    path('update_publication/<int:pk>', UpdatePublicationView.as_view(), name='update_publication'),
    path('delete_publication', delete_publication, name='delete_publication'),
]
