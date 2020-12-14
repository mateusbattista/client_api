from django.db import models

# Create your models here.

SERVICOS = [
    ('LF','Lógica Flow'),
    ('LA','Lógica For Assinantes'),
    ('LE','Lógica ERP'),
    ('LT','Lógica for Técnicos'),
    ('LP','Lógica Fone'),
    ('LC','Lógica Active'),

]


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    servico_interessado = models.CharField(max_length=2, choices=SERVICOS,default='LE')

    def __str__(self):
        return self.nome