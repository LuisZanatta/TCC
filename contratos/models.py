from django.db import models
from django.contrib.auth.models import User


class Contrato (models.Model):
    TIPOS_CONTRATO_CHOICES = [
        ('1', 'Serviços'),
        ('2', 'Produtos'),
    ]

    STATUS_CHOICES = [
        ('1', 'Ativo'),
        ('2', 'Concluido'),
        ('3', 'Cancelado'),
    ]

    numero_contrato = models.CharField(max_length=50, verbose_name="Nome do contrato:")
    valor = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Valor:")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    data_inicio = models.DateField(verbose_name="Data de Inicio:")
    data_fim = models.DateField(verbose_name="Data de Término:")
    tipo = models.CharField(max_length=1, choices=TIPOS_CONTRATO_CHOICES, verbose_name="Tipo")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1', verbose_name="Status")
    motivo_cancelamento = models.TextField(null=True, blank=True, verbose_name="Motivo do Cancelamento:")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivo = models.FileField(upload_to='contratos/', verbose_name="Arquivo do Contrato:")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # se for um serviço
    descricao_servico = models.TextField(null=True, blank=True)
    # se for um produto
    descricao_produto = models.TextField(null=True, blank=True)
    tipo_produto = models.CharField(max_length=200, null=True, blank=True)
    quantidade_produto = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.numero_contrato

    def aditivos(self):
        return Aditivo.objects.filter(contrato_id = self)


class Aditivo(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    descricao = models.TextField(null=True, blank=True)
    arquivo = models.FileField(upload_to='aditivos')

    def __str__(self):
        return "Contrato Aditivo Referente ao Contrato " + self.contrato.numero_contrato