from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User , unique = True)
    phone_number = models.CharField(max_length = 20)