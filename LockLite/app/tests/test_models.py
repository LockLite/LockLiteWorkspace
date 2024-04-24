from django.test import TestCase
import pytest
from django.test import Client
from app.models import Credential

class CredentialTestCase(TestCase):
	def testCredential(self):
		credential = Credential.objects.create(
			credentials_email="test@test.com",
			credentials_password="gAAAAABmBCTUUoR-Px2vWPoLENI3da2TcV847a9u0-arMClWUEbz2gHSyye0NZQzuIg36MtzvAe_xzqkHLYEUEuu9kD791A9RQ==",
			label="test.com",
			user="1"
		)
		expected_value = "test@test.com | test | test.com | 1"
		assert str(credential) == expected_value


