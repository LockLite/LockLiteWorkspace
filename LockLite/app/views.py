from django.shortcuts import render

from .models import User


# Create your views here.
def index(request, *args, **kwargs):
	return render(request, 'index.html')


def test(request, *args, **kwargs):
	users = User.objects.all()
	data = {
		'name': "Test",
		'users': users
	}
	return render(request, 'test.html', data)
