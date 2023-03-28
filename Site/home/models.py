from django.db import models

class Comodo(models.Model):
    comodo = models.CharField(max_length=50)
    iluminacao = models.BooleanField(default=False)
    ventilacao = models.IntegerField(default=0)
    

# Create your models here.
