from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^rephrase', views.rephrase, name='rephrase'),
	url(r'^contact', views.rephrase, name='rephrase'),
	url(r'^page', views.rephrase, name='rephrase'),
    url(r'^$', views.rephrase, name='rephrase'),
]