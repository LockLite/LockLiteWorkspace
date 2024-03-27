from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.conf import settings

class Credential(models.Model):
	credentials_email = models.CharField(max_length=50)
	credentials_password = models.CharField(max_length=120)
	label = models.CharField(max_length=50)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	@property
	def pswd_decrypted(self):
		f = Fernet(settings.ENCRYPT_KEY)
		credential_decrypted = f.decrypt(self.credentials_password)
		credential_decoded = credential_decrypted.decode('utf-8')
		return credential_decoded

	def __str__(self):
		return self.label

