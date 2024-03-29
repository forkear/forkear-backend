from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.public.views import home

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('account/', include('apps.account.urls')), 
    path('api/', include('apps.api.urls')), 
]


if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
