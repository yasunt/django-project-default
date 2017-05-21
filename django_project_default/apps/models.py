from django.db import models

from accounts.models import CustomUser


class Tag(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=20)


class Something(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(CustomUser)
    tags = models.ManyToManyField(Tag)
