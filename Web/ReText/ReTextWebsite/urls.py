from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^rephrase', views.rephrase, name='rephrase'),
	url(r'^contact', views.rephrase, name='rephrase'),
	url(r'^page', views.rephrase, name='rephrase'),
    url(r'^$', views.rephrase, name='rephrase'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)