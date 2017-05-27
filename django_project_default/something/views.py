import json
import math

from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http.response import JsonResponse
from django.core.urlresolvers import reverse, reverse_lazy

from braces.views import UserFormKwargsMixin

from .models import Something, Tag
from .forms import SomethingPostForm


class AuthorValidTestMixin(UserPassesTestMixin):
    '''Raise permission error if request-user dosen't equal object author.'''

    def test_func(self):
        if not self.request.user ==  self.get_object().user:
            print('You: {0}, Author: {1}'.format(self.request.user, self.get_object().user))
            raise PermissionError('You are not object author.')
        else:
            return True


class PaginateMixin(View):
    '''Mixin which implements pagination.
    You have to define a model class variable in child class.'''

    def get_queryset(self):
        page = self.kwargs.get('page')
        if page:
            page = int(page)
            queryset = self.__class__.model.objects.all()[10*(page-1):10*page]
        else:
            queryset = self.__class__.model.objects.all()[:10]
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = list(range(1, (math.ceil(self.__class__.model.objects.count() / 10)+1)))
        return context


class ObjectListView(PaginateMixin, ListView):

    template_name = 'something/list.html'
    queryset = Something.objects.all()
    model = Something
    context_object_name = 'object_list'


class ObjectListJsonResponseView(View):

    def get(self, request):
        return JsonResponse({'object_list': json.dumps(serializers.serialize('json', Something.objects.all()))})


class ObjectFilterbyTagView(PaginateMixin, ListView):

    template_name ='something/list.html'
    model = Something

    def get_queryset(self):
        tag = get_object_or_404(Tag, id=self.kwargs['tag_id'])
        return tag.something_set.all() if tag else None


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


class ObjectUpdateView(LoginRequiredMixin, AuthorValidTestMixin, UserFormKwargsMixin, UpdateView):

    model = Something
    form_class = SomethingPostForm
    template_name = 'something/update.html'
    success_url = reverse_lazy('something:list')

    def get_object(self):
        obj = super().get_object()
        print(obj)
        return obj

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        tag_id = self.request.POST.get('tags')
        if tag_id:
            kwargs['tags'] = Tag.objects.filter(id=tag_id)
        return kwargs


class ObjectDeleteView(LoginRequiredMixin, AuthorValidTestMixin, UserFormKwargsMixin, DeleteView):

    model = Something
    success_url = reverse_lazy('something:list')
