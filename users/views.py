from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

# Create your views here.
class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	sucess_url = reverse_lazy('home')
	template_name = 'signup.html'