from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from .views import IndexView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^something/', include('something.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include('registration.backends.hmac.urls')),
    url(r'^$', IndexView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
