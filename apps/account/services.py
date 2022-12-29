#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db import transaction


class UserService:
    
    @transaction.atomic
    def create(
        self,
        username:str,
        email:str,
        password:str) -> User:

        user = User.objects.create(
            username=username,
            email=email
        )

        user.set_password(password)
        
        user.save()

        return user
    
    