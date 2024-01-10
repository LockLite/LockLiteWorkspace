from django.db import models


class User(models.Model):
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_email


class Credential(models.Model):
    credentials_email = models.CharField(max_length=50)
    credentials_password = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
