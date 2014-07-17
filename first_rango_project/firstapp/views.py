from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from firstapp.forms import CategoryForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from firstapp.dota_stats import get_stats
from datetime import datetime
from steam import get_profile_picture
from steam2 import generate_random_steamid, generate_random_steamid_wpicture, get_person_name
import random
# Create your views here.

def index(request):

	request.session.set_test_cookie()

	context = RequestContext(request)
	context_dict = {'boldmessage':request}
	
	response = render_to_response('firstapp/index.html', context_dict, context)
	'''visits = int(request.COOKIES.get('visits', '0'))
	
	if 'last_visit' in request.COOKIES:
		last_visit = request.COOKIES['last_visit']
		last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")	
		response.set_cookie('visits', visits+1)
		response.set_cookie('visits', visits+1)
		if(datetime.now() - last_visit_time).days > 0:	
			response.set_cookie('visits', visits+1)
			response.set_cookie('last_visit', datetime.now())
	
	else: 
		response.set_cookie('last_visit', datetime.now())	
	'''
	visits=0
	if request.session.get('last_visit'):
		last_visit_time = request.session.get('last_visit')
		visits = request.session.get('visits', 0)
		
		if(datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).seconds > 5 :
			request.session['visits'] = visits + 1
			request.session['last_visit'] = str(datetime.now())
	else:
		request.session['last_visit'] = str(datetime.now())
		request.session['visits'] = 1
	if visits > 10:
		context_dict['cookies']="You have visited this site over 10 times"

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
	
	if request.session.test_cookie_worked():
		print ">>>> TEST COOKIE WORKED"
		request.session.delete_test_cookie()
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




def update_stats(request):
        context=RequestContext(request)

        result_list=[1]
	profile_picture_url=None
        if request.method=='POST':
                profile_picture_url=get_profile_picture(vanityurl="mrpuckmrpuck")
        return render_to_response('firstapp/new_game.html', {'profile_picture_url': profile_picture_url}, context)


def profile_picture_game(request):
	context=RequestContext(request)

	profile_picture_url=None
	steam_id=generate_random_steamid_wpicture()
	person_name=get_person_name(steam_id)
	random_names=[get_person_name(generate_random_steamid()),get_person_name(generate_random_steamid()),get_person_name(generate_random_steamid())]
	profile_picture_url=get_profile_picture(steam_id=steam_id)

	random_names.append(person_name)
	random.shuffle(random_names)

	return render_to_response('firstapp/picture_game.html',{
	    'profile_picture_url':profile_picture_url,
	    'random_name1':random_names[0],
	    'random_name2':random_names[1],
	    'random_name3':random_names[2],
	    'random_name4':random_names[3],
	    'person_name':person_name}, context)
	
