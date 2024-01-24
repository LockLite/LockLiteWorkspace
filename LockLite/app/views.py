from django.contrib.auth.models import User

# Create your views here.
def index(request, *args, **kwargs):
	return render(request, 'index.jinja')


def test(request, *args, **kwargs):
	users = User.objects.all()
	data = {
		'name': "Test",
		'users': users
	}
	return render(request, 'test.jinja', data)
