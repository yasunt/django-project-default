from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Something, Tag


class ObjectListView(ListView):

    template_name = 'apps/list.html'
    queryset = Something.objects.all()
    context_object_name = 'object_list'


class ObjectDetailView(DetailView):

    template_name = 'apps/detail.html'
    model = Something
