from django.shortcuts import render

# Create your views here.
def home_page(request):
	return render(request=request, template_name='movieapp/homepage.html')

from movieapp.forms import Moviedetailsform
def add_movie(request):
	movie_form=Moviedetailsform()

	if request.method=='POST':
		movie_form=Moviedetailsform(request.POST)
		if movie_form.is_valid():
			movie_form.save(commit=True)

	if request.method=='POST':
		movie_form=Moviedetailsform(request.POST)
		if movie_form.is_valid():
			print(f'moviename:{movie_form.cleaned_data["moviename"]}')
			print(f'hero:{movie_form.cleaned_data["hero"]}')
			print(f'heroine:{movie_form.cleaned_data["heroine"]}')
			print(f'rating:{movie_form.cleaned_data["rating"]}')

	my_dict={'movie_form':movie_form}
	return render(request=request, template_name='movieapp/addmovie.html',context=my_dict)

from movieapp.models import Moviedetails

def movie_list(request):
	data=Moviedetails.objects.all()
	dict_val={'data':data}
	return render(request=request, template_name='movieapp/movielist.html',context=dict_val)
