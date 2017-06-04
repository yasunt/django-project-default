from django import forms
from django.forms import ModelForm, formset_factory

from core.forms import UserPostFormMixin

from .models import Something, UserPostImage


class SomethingPostForm(UserPostFormMixin, ModelForm):

    class Meta:
        model = Something
        fields = ('name', 'description', 'tags')


class UserPostImageForm(ModelForm):

    image = forms.ImageField(label='image')

    class Meta:
        model = UserPostImage
        fields = ('image', )


UserPostImageFormSet = formset_factory(UserPostImageForm, extra=2)
