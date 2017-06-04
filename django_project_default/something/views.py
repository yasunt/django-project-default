import json
import math

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http.response import JsonResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms import formset_factory

from braces.views import UserFormKwargsMixin

from .models import Something, Tag, UserPostImage
from .forms import SomethingPostForm, UserPostImageForm, UserPostImageFormSet


class AuthorValidTestMixin(UserPassesTestMixin):
    """
    Raise permission error if request-user dosen't equal object author.
    """

    def test_func(self):
        if not self.request.user ==  self.get_object().user:
            raise PermissionError('You are not object author.')
        else:
            return True


class ObjectListView(ListView):

    template_name = 'something/list.html'
    queryset = Something.objects.all()
    model = Something
    context_object_name = 'object_list'
    paginate_by = 10


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

    def post(self, request):
        something_form = SomethingPostForm(**self.get_form_kwargs())
        formset = UserPostImageFormSet(request.POST, request.FILES)

        if something_form.is_valid():
            if formset.is_valid():
                something = something_form.save()

                for form in formset.cleaned_data:
                    if not form:
                        continue
                    image = UserPostImage(image=form['image'], something=something)
                    image.save()
            else:
                raise TypeError('Uploaing files contain non-image files.')
        else:
            # implement error handling operation
            raise ValidationError('Posted content is not valid.')

        return redirect(self.get_success_url())

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        tag_id = self.request.POST.get('tags')
        if tag_id:
            kwargs['tags'] = Tag.objects.filter(id=tag_id)
        return kwargs

    def get_context_data(self):
        context = super().get_context_data()
        context['image_formset'] = UserPostImageFormSet
        return context

    def get_success_url(self):
        return reverse('something:list')


class ObjectUpdateView(LoginRequiredMixin, AuthorValidTestMixin, UserFormKwargsMixin, UpdateView):

    model = Something
    form_class = SomethingPostForm
    template_name = 'something/update.html'
    success_url = reverse_lazy('something:list')

    def get_object(self):
        obj = super().get_object()
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


class ObjectSearchView(ListView):

    template_name = 'something/search.html'
    paginate_by = 10

    def get_queryset(self):
        query = Q()
        tag_id = self.request.GET.get('tag_id')
        tag = get_object_or_404(Tag, id=tag_id) if tag_id else None
        query = query & Q(tags=tag) if tag else query
        name_contains = self.request.GET.get('q')
        query = query & Q(name__contains=name_contains) if name_contains else query
        return Something.objects.filter(query)

    def get_context_data(self):
        context = super().get_context_data()
        query_dict = {key: value for key, value in self.request.GET.items()}
        context.update(query_dict)
        return context
