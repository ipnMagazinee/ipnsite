""" ipnsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path, include
from ipnsite import settings

urlpatterns = [
    # django urls
    path('admin/', admin.site.urls),
    # my urls
    path('account/', include('apps.account.urls')),  # account
    path('user/', include('apps.user.urls')),  # user
    path('editor/', include('apps.editor.urls')),  # editor
    path('publisher/', include('apps.publisher.urls')),  # publisher
    path('direction/', include('apps.direction.urls')),  # publisher
    path('settings/', include('apps.settings.urls')),  # settings
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
