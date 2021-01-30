from django.db import models


class Endereco(models.Model):
    linha1 = models.CharField(max_length=150)
    linha2 = models.CharField(max_length=150, null=True, blank=True)
    cidade = models.CharField(max_length=50)  # todo: fazer com choices para cada estado de cidade relaionado a pais, Ex
    estado = models.CharField(max_length=50)  # todo: altos é do piauí, e piauí que é do brasil.
    pais = models.CharField(max_length=50)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.linha1
