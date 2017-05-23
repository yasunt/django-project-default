from django.conf.urls import url, include

from .views import ObjectDetailView, ObjectListView, ObjectCreateView
from .views import ObjectListJsonResponseView, ObjectDetailJsonResponseView


app_name = 'something'

urlpatterns = [
    url(r'^list/', ObjectListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>\w+)/', ObjectDetailView.as_view(), name='detail'),
    url(r'^create/', ObjectCreateView.as_view(), name='create'),
]
