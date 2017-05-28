from django.conf.urls import url, include

from .views import ObjectDetailView, ObjectListView, ObjectCreateView, ObjectUpdateView, ObjectDeleteView
from .views import ObjectSearchView
from .views import ObjectListJsonResponseView, ObjectDetailJsonResponseView


app_name = 'something'

urlpatterns = [
    url(r'^list/', ObjectListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>\w+)/', ObjectDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>\w+)', ObjectUpdateView.as_view(), name='update'),
    url(r'^create/', ObjectCreateView.as_view(), name='create'),
    url(r'^delete/(?P<pk>\w+)/', ObjectDeleteView.as_view(), name='delete'),
    url(r'^search/', ObjectSearchView.as_view(), name='search'),
]
