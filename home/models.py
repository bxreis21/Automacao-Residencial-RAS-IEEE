from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    name = models.CharField(max_length=30, verbose_name='Cômodo')
    status = models.BooleanField(verbose_name='Status')

    def __str__(self) -> str:
        return self.name
    
class Device(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Cômodo')
    name = models.CharField(max_length=30, verbose_name='Nome do Dispostivo')
    status = models.BooleanField(verbose_name='Status do Dispositivo')
    porta = models.SmallIntegerField('Porta do ESP32')
    pwm = models.IntegerField(verbose_name='PWM', default=0, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
