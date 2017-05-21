from django.conf.urls import url, include

from .views import ObjectDetailView, ObjectListView


app_name = 'apps'

urlpatterns = [
    url(r'^list/', ObjectListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>\w+)/', ObjectDetailView.as_view(), name='detail'),
]
