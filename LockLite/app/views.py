from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from .models import User

def index(request, *args, **kwargs):
	return render(request, 'index.jinja')


def test(request, *args, **kwargs):
	users = User.objects.all()
	data = {
		'name': "Test",
		'users': users
	}
	return render(request, 'test.jinja', data)


def register(request, *args, **kwargs):
	if request.method == 'GET':
		form = RegisterForm()
		return render(request, 'registration/register.html', {'form': form})
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.username.lower()
			user.save()
			messages.success(request, 'You have signed up successfully.')
			login(request, user)
			return redirect('/')
		else:
			return render(request, 'registration/register.html', {'form': form})

def homepage(request, *args, **kwargs):
	current_user = request.user
	user = User.objects.get(id=current_user.id)
	data = {
		'name': "Home",
		'user': user
	}
	return render(request, 'homepage.html', data)
