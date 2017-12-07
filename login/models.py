from django.db import models

# Create your models here.
class registro(models.Model):
    nombre = models.CharField(max_length=60)
    usuario = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    nivel = models.SmallIntegerField()

class claves(models.Model):
    clave = models.SmallIntegerField()
    nivel = models.SmallIntegerField()


