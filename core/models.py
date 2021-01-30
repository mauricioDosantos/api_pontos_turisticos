from django.db import models
from comentario.models import Comentario
from atracao.models import Atracao
from avaliacao.models import Avaliacao
from endereco.models import Endereco


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    avaliacoes = models.ManyToManyField(Avaliacao)
    comentarios = models.ManyToManyField(Comentario)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
