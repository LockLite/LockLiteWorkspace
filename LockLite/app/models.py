from django.db import models


# Create your models here.
class User(models.Model):
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)


class Credential(models.Model):
    credentials_email = models.CharField(max_length=50)
    credentials_password = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
