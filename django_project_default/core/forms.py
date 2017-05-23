from django.forms import ModelForm

from braces.forms import UserKwargModelFormMixin


class UserPostFormMixin(UserKwargModelFormMixin, ModelForm):

    def __init__(self, *args, **kwargs):
        self.tags = kwargs.pop('tags', None)
        super().__init__(*args, **kwargs)

    def save(self, orce_insert=False, force_update=False, commit=True):
        obj = super().save(commit=False)
        obj.user = self.user
        if commit:
            obj.save()
        obj.tags = self.tags
        return obj
