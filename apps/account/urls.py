#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.urls import path, include
from .views import account_root
from .views import RegisterView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', account_root, name='account_root'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='account_register'),
    path('api-auth/', include('rest_framework.urls')),
]