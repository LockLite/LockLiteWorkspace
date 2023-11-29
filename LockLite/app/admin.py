from django.contrib import admin
from .models import User
from .models import Credential

# Register your models here.
admin.site.register(User)
admin.site.register(Credential)