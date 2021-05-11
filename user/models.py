from django.db import models


class UserForm(models.Model):

    username = models.CharField(max_length=50)
    email = models.EmailField()


class User(models.Model):
    username = models.CharField(max_length=125)
    email = models.CharField(max_length=125)
