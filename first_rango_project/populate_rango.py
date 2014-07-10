import os

def populate():
	python_cat = add_cat('Python')
	
	add_page(cat=python_cat, title="How to python", url="http://docs.python.org/2/tutorial/")
	
	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print "- {0} - {1}".format(str(c), str(p))




def add_page(cat, title, url, views=0):
	p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
	return p

def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	return c

if __name__ == '__main__':
	print "Starting population script for [Rango]..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_rango_project.settings')
	from firstapp.models import Category, Page
	populate()
