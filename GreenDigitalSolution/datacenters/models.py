from django.db import models

class DataCenter(models.Model):

    DEFINICAO =(
        ('0', 'Não sustentável'),
        ('1', 'Sustentável')
    )
    titulo = models.CharField(max_length=255, default='')
    descricao = models.TextField()
    categoria = models.CharField(max_length=255)
    sustentavel = models.CharField(
        max_length=1,
        choices=DEFINICAO,
    )
    preco = models.DecimalField(max_digits=9999, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    setor = models.CharField(max_length=255, default='')
    consumo_eletrico = models.IntegerField(default = 0)
    def __str__(self):
        return self.titulo
    