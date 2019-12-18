
from django.urls import path
# views
from apps.publisher.views import *

app_name = 'publisher'

urlpatterns = [
    path('<str:name>/', PublisherView.as_view(), name='publisher'),
    path('new_publication/<str:name>', NewPublicationView.as_view(), name='new_publication'),
    path('update_publication/<int:pk>', UpdatePublicationView.as_view(), name='update_publication'),
    path('delete_publication', delete_publication, name='delete_publication'),
]
