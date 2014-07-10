from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from bushstats.models import Player
#from bushstats.bing_search import run_query
import bushstats.bing_search
from bushstats.dota_stats import get_stats


def index(request):
	context = RequestContext(request)
	#return HttpResponse("HI")
	context_dict = {'paragraph': "Initializing subterfuge flux capacitors undermine your kids high school diploma",
                        "title": "Welcome To Bushleague"}
	return render_to_response('bushstats/index.html', context_dict, context)

def stats(request):
	return render(request, "bushstats/stats.html", {"stats": Player.objects.all()})

def new_game(request):
	
	return render(request, 'bushstats/new_game') 

def search(request):
	context = RequestContext(request)
	result_list=[]
	if request.method=='POST':
		query=request.POST['query'].strip()
		
		if query:
			result_list=run_query(query)
	return render_to_response('bushstats/search.html', {'result_list': result_list},context) 	

def update_stats(request):
	context=RequestContext(request)
	result_list=[1]
	if request.method=='POST':
		result_list=get_stats("Mr.Puck")
	return render_to_response('bushstats/new_game.html', {'result_list': result_list}, context)
