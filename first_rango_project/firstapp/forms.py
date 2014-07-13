from django import forms
from django.contrib.auth.models import User
from firstapp.models import Page, Category, UserProfile

#why did you have to specify views/likes in categoryform but for some reason in UserProfileForm it is assumed automatically handles by attributes from the model it is based upon
#maybe its only to update as the model maybe has all the input methods defaulted to some undesirable kind like the visible to invisible passsword

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter the category name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # An inline class to provide additional information on the form.
	class Meta:
        # Provide an association between the ModelForm and a model
		model = Category

class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Please enter title")
	url = forms.CharField(max_length=200, help_text="enter url")
	views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	
	
	class Meta:

		model = Page
		#Fields that we include in our form
		#hiding foreign keys
		fields = ('title', 'url', 'views')
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
	
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture')

