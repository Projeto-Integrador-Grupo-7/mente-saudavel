from django.db import models
from django.utils import timezone
from usuario.models import Usuario  # Certo importar assim

class Formulario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pontuacao = models.IntegerField()
    estratificacao = models.SmallIntegerField()
    data_formulario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Formulario {self.id} - Usuario {self.usuario.id}'

class Resposta(models.Model):
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    numero = models.IntegerField()
    valor = models.SmallIntegerField()

    def __str__(self):
        return f'Resposta {self.numero} do Formulário {self.formulario.id}'
