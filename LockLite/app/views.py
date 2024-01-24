from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm


def register(request, *args, **kwargs):
	if request.method == 'GET':
		form = RegisterForm()
		return render(request, 'registration/register.jinja', {'form': form})
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.username.lower()
			user.save()
			messages.success(request, 'You have signed up successfully.')
			login(request, user)
			return redirect('login')
		else:
			return render(request, 'registration/register.jinja', {'form': form})


@login_required(login_url="login")
def index(request, *args, **kwargs):
	data = {
		'name': request.user.username,
		'user': request.user.email
	}
	return render(request, 'index.jinja', data)
