from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()

    def __str__(self):
        return 'Perfil de Usuario: {}'.format(self.user.username)


