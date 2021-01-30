from django.db import models


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_funcionamento = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    idade_min = models.IntegerField()
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome