from __future__ import unicode_literals

from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

class Transacao(models.Model):
    data_hora = models.DateTimeField()
    descricao = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria)
    valor = models.DecimalField(max_digits=11, decimal_places=2)