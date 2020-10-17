from django import forms
from movieapp.models import Moviedetails

class Moviedetailsform(forms.ModelForm):
    class Meta:
    	model= Moviedetails
    	fields=('moviename','hero','heroine','rating')
    