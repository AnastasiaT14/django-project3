from django.db import models

class User(models.Model):
    username = models.CharField(default='User Name', max_length=20)
    lastname = models.CharField(default='User Lastname', max_length=20)
    age = models.IntegerField()
    email = models.EmailField()