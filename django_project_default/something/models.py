from django.db import models

from core.models import TimeStampedModel
from accounts.models import CustomUser


class Tag(TimeStampedModel):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=20)


class Something(TimeStampedModel):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(CustomUser)
    tags = models.ManyToManyField(Tag)


class UserPostImage(TimeStampedModel):

    image = models.ImageField(upload_to='media/something/', blank=True)
    something = models.ForeignKey(Something)
