from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^rephrase', views.rephrase, name='rephrase'),
	url(r'^rephrase/text(?P<text>[\W]+)/$', views.rephrase, name='rephrase'),
	url(r'^contact', views.rephrase, name='contact'),
	url(r'^page', views.rephrase, name='home'),
    url(r'^$', views.rephrase, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)