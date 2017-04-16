from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template
from django.core.urlresolvers import resolve
import os
from generate import *

def index(request):
    return HttpResponse("Hello, world. You're at the ReText index.")
	
def rephrase(request, text=""):
	context = Context({"my_name": "Lummie"})
	text = request.GET.get('text', '')
	print ("text: "+ text)
	if text != "":
		generate(text).create_page()
		print ("newRephrase sent")
		template = loader.get_template('ReTextWebsite/newindex.html')
	else:
		print ("rephrase sent")
		template = loader.get_template('ReTextWebsite/index.html')
	return HttpResponse(template.render(context, request))