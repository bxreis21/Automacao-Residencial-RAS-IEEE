from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    status = models.BooleanField()

# Create your models here.

