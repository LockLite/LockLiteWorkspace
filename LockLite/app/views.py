from django.shortcuts import render

from .models import User


# Create your views here.
def index(request, *args, **kwargs):
	test = User.objects.all()
	data = {
		'name': "Test",
		'users': test
	}
	return render(request, 'index.html', data)
