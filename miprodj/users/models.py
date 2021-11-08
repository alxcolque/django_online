from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    #para imprimir los objetos
    def __str__(self) :
        return self.name