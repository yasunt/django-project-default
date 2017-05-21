from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.shortcuts import get_object_or_404


class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

    def join_some_group(self):
        group = get_object_or_404(Group, name='some_group')
        self.groups.add(group)
