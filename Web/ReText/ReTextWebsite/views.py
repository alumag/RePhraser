from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template
import os

def index(request):
    return HttpResponse("Hello, world. You're at the ReText index.")
	
def rephrase(request):
	context = Context({"my_name": "Lummie"})
	template = loader.get_template('ReTextWebsite/rephrase.html')
	return HttpResponse(template.render(context, request))