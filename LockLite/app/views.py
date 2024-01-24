from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from .models import User

def index(request, *args, **kwargs):
	return render(request, 'index.jinja')


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
			return redirect('login')
		else:
			return render(request, 'registration/register.html', {'form': form})

@login_required(login_url="login")
def dashboard(request, *args, **kwargs):
	user = User.objects.get(id=2)
	user_email = user.email
	data = {
		'name': "Dashboard",
		'user': user_email
	}
	return render(request, 'dashboard.jinja', data)
