from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context = RequestContext(request)
	#return HttpResponse("HI")
	context_dict = {'paragraph': "Initializing subterfuge flux capacitors undermine your kids high school diploma",
                        "title": "Welcome To Bushleague"}
	return render_to_response('bushstats/index.html', context_dict, context)
