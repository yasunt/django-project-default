import json

from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http.response import JsonResponse
from django.core.urlresolvers import reverse

from braces.views import UserFormKwargsMixin

from .models import Something, Tag
from .forms import SomethingPostForm


class CreatorValidTestMixin(UserPassesTestMixin):

    def test_func(self):
        if not self.request.user ==  self.object.user:
            raise PermissionError
        else:
            return True


class ObjectListView(ListView):

    template_name = 'something/list.html'
    queryset = Something.objects.all()
    context_object_name = 'object_list'


class ObjectListJsonResponseView(View):

    def get(self, request):
        return JsonResponse({'object_list': json.dumps(serializers.serialize('json', Something.objects.all()))})


class ObjectDetailView(DetailView):

    template_name = 'something/detail.html'
    model = Something


class ObjectDetailJsonResponseView(View):

    def get(self, request, pk):
        return JsonResponse({'object': serializers.serialize('json', Something.objects.filter(pk=pk))})


class ObjectCreateView(LoginRequiredMixin, UserFormKwargsMixin, CreateView):

    form_class = SomethingPostForm
    template_name = 'something/create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        tag_id = self.request.POST.get('tags')
        if tag_id:
            kwargs['tags'] = Tag.objects.filter(id=tag_id)
        return kwargs

    def get_success_url(self):
        return reverse('something:list')


class ObjectUpdateView(LoginRequiredMixin, UserFormKwargsMixin, UpdateView):

    pass


class ObjectDeleteView(LoginRequiredMixin, UserFormKwargsMixin, DeleteView):

    pass
