#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from  django.db import models
from django.contrib.auth.models import User
from typing import Iterable


def user_list() -> Iterable[User]:
    return User.objects.all()
