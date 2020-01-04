
from django.urls import path
# views
from apps.publisher.views import *

app_name = 'publisher'

urlpatterns = [
    path('<str:name>/', PublisherView.as_view(), name='publisher'),
    path('<str:name>/<int:id_publication>', Publish.as_view(), name='publish'),
    path('download_image/<int:image_id>/', download_image, name='download_image'),
]
