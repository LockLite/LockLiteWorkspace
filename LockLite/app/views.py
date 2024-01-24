from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from .models import Credential


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
	print(request.user.id)
	print(Credential.objects.filter(user_id=request.user.id).values())
	data = {
		'name': request.user.username,
		'user': request.user.email,
		'credentials': Credential.objects.filter(user_id=request.user.id).values()
	}
	return render(request, 'index.jinja', data)
