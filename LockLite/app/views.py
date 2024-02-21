from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .forms import AddCredentialForm
from .models import Credential


class CustomLoginView(LoginView):
	authentication_form = LoginForm
	link_page = "register"
	template_name = 'form.jinja'
	extra_context = {
		'title': "Login",
		'link': {
			'text': "Don't have an account?",
			'name': link_page.capitalize(),
			'page': link_page
		}
	}


def register(request, *args, **kwargs):
	link_page = "login"
	context = {
		'title': "Register",
		'link': {
			'text': "Already has an account?",
			'name': link_page.capitalize(),
			'page': link_page
		}
	}
	if request.method == 'GET':
		context['form'] = RegisterForm()
		return render(request, 'form.jinja', context)
	if request.method == 'POST':
		context['form'] = RegisterForm(request.POST)
		if context['form'].is_valid():
			user = context['form'].save(commit=False)
			user.username = user.username.lower()
			user.save()
			messages.success(request, 'You have signed up successfully.')
			login(request, user)
			return redirect(link_page)
		else:
			return render(request, 'form.jinja', context)


@login_required(login_url="login")
def index(request, *args, **kwargs):
	data = {
		'name': request.user.username,
		'user': request.user.email,
		'credentials': Credential.objects.filter(user_id=request.user.id).values()
	}
	return render(request, 'index.jinja', data)


@login_required(login_url="login")
def createcred(request):
	link_page = "index"
	context = {
		'title': "Create credential",
		'link': {
			'text': "Show credentials",
			'name': "here",
			'page': link_page
		}
	}
	if request.method == 'POST':
		context['form'] = AddCredentialForm(request.POST)
		if context['form'].is_valid():
			credential = context['form'].save(commit=False)
			credential.user = request.user
			credential.save()
			return redirect('index')
		else:
			return render(request, 'form.jinja', context)
	else:
		context['form'] = AddCredentialForm()
		return render(request, 'form.jinja', context)
