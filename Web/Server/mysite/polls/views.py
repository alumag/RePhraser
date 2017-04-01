from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader


def index(request):
	try:
		#template = loader.get_template('polls/hey.txt')
		#context = {'Lummie'}
		#return HttpResponse(template.render(context, request))
		return render(request, 'hey.txt')
	except Exception as inst:
		raise Http404(type(inst), inst)
    #return HttpResponse("Hello, world. You're at the polls index.")
	
def hello(request):
	return HttpResponse("Hello, world. You're at the polls index.")