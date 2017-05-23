from django.forms import ModelForm

from core.forms import UserPostFormMixin

from .models import Something

class SomethingPostForm(UserPostFormMixin, ModelForm):

    class Meta:
        model = Something
        fields = ('name', 'description', 'tags')
