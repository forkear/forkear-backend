from django.urls import include, path

from .views import api_root

urlpatterns = [
    path('', api_root, name='api_root'),
] 