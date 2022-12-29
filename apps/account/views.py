#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework.validators import UniqueValidator
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.account.selectors import user_list
from apps.account.services import UserService



@api_view(['GET'])
@permission_classes([AllowAny])
def account_root(request, format=None):
    return Response({
        'login':reverse('token_obtain_pair', request=request, format=format), 
        'refresh token':reverse('token_refresh', request=request, format=format), 
        'register':reverse('account_register', request=request, format=format), 
    })
    
    




class RegisterView(generics.CreateAPIView):


    class RegisterSerializer(serializers.ModelSerializer):

        email = serializers.EmailField(
                required=True,
                validators=[UniqueValidator(queryset=user_list())]
        )

        password = serializers.CharField(
                write_only=True, 
                required=True, 
                validators=[validate_password],
                style={'input_type': 'password'}
        )

        password2 = serializers.CharField(
                write_only=True, 
                required=True,
                style={'input_type': 'password'}
        )

        class Meta:
            model = User
            fields = ('username', 'password', 'password2', 'email')

        def validate(self, attrs):
            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError({"password": "Password fields didn't match."})

            return attrs

        def create(self, validated_data):
            
            user_service = UserService()
            
            user = user_service.create(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )
            
            return user
            
        
    queryset = user_list(),
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    