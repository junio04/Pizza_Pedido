from django.db import models
from django.utils import timezone


class Cliente(models.Model):

    nome = models.CharField(max_length= 100, null=False, blank=False)
    telefone = models.CharField(max_length=25, blank=True, null=False)
    email = models.EmailField(null=False, blank=False, )
    endereco = models.CharField(max_length= 200, blank=True, null=False)
    cidade = models.CharField(max_length= 100, blank=True, null=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome}  {self.endereco} {self.cidade}'

class Pizza(models.Model):
    TAMANHO_CHOICES = [
        ('pequena', 'Pequena'),
        ('media', 'Média'),
        ('grande', 'Grande'),
    ]

    tamanho = models.CharField(max_length=20, choices=TAMANHO_CHOICES)
    valor = models.DecimalField(max_digits=5, decimal_places=2)


class Refrigerante(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=5, decimal_places=2)











