from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template
from django.core.urlresolvers import resolve
import os

def index(request):
    return HttpResponse("Hello, world. You're at the ReText index.")
	
def rephrase(request, text=""):
	context = Context({"my_name": "Lummie"})
	text = request.GET.get('text', '')
	print ("text: "+ text)
	if text != "":
		print(os.path.dirname(os.path.realpath(__file__)))
		file = open((os.path.dirname(os.path.realpath(__file__))+"\templates\ReTextWebsite\rephrase.html"), 'r')
		newfile = open(os.path.dirname(os.path.realpath(__file__))+"\templates\ReTextWebsite\newRephrase.html", "w")
		newfile.write(file.read().replace("<ul id=\"msg\"> </ul>", text))
		newfile.close()
		file.close()
		template = loader.get_template('ReTextWebsite/newRephrase.html')
	else:
		template = loader.get_template('ReTextWebsite/rephrase.html')
	return HttpResponse(template.render(context, request))
	
def home(request):
	context = Context({"my_name": "Lummie"})
	template = loader.get_template('ReTextWebsite/page.html')
	return HttpResponse(template.render(context, request))
	
def contact(request):
	context = Context({"my_name": "Lummie"})
	template = loader.get_template('ReTextWebsite/contact.html')
	return HttpResponse(template.render(context, request))