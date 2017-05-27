from django.conf.urls import url, include

from .views import ObjectDetailView, ObjectListView, ObjectCreateView, ObjectUpdateView, ObjectDeleteView
from .views import ObjectFilterbyTagView
from .views import ObjectListJsonResponseView, ObjectDetailJsonResponseView


app_name = 'something'

urlpatterns = [
    url(r'^list/(page/)*(?P<page>\d*)', ObjectListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>\w+)/', ObjectDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>\w+)', ObjectUpdateView.as_view(), name='update'),
    url(r'^create/', ObjectCreateView.as_view(), name='create'),
    url(r'^delete/(?P<pk>\w+)/', ObjectDeleteView.as_view(), name='delete'),
    url(r'^tag/(?P<tag_id>\w+)', ObjectFilterbyTagView.as_view(), name='tag'),
]
