from django import forms
from firstapp.models import Page, Category

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
