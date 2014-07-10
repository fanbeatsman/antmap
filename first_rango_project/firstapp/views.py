from django.shortcuts import render
from django.http import HttpResponse 
from django.template import RequestContext
from django.shortcuts import render_to_response
from firstapp.forms import CategoryForm
# Create your views here.

def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':request}
	return render_to_response('firstapp/index.html', context_dict, context)
def about(request):
	return HttpResponse("A good app needs no about page")

def add_category(request):
	context = RequestContext(request)
	
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		
		if form.is_valid():
			form.save(commit=True)
			print form.errors
			return index(request)
		else:
			print form.errors
	else:
		form = CategoryForm()
	return render_to_response('firstapp/add_category.html', {'form': form}, context)

	
