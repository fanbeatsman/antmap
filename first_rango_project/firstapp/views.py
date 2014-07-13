from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from firstapp.forms import CategoryForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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

def register(request):
	context = RequestContext(request)
	
	registered=False
	
	if request.method=='POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			#why am i changing around the storing variables, for example this user from user_form
			user.set_password(user.password)
			user.save()
			
			#Set comit to False cause we need to set the user attrivutes ourselves
			profile = profile_form.save(commit=False)
			profile.user = user
			
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			#when here its obvious the save method can save into the original variable instead of returning it to another

			profile.save()
			
			registered = True
		#couldnt I just use try and except?
		else:
			print user_form.errors, profile_form.errors


	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render_to_response(
	    'firstapp/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)
def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		#using django's authentication machinery, return an actual user object if auth worked
		user = authenticate(username=username, password=password)
		
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/firstapp/')
			else: 
				return HttpResponse("Your account is disabled")
		else: 
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid username/password")
	
	else:
		return render_to_response('firstapp/login.html', {}, context)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/firstapp/')
