from django.shortcuts import render , redirect
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(response):
	return redirect("login")

