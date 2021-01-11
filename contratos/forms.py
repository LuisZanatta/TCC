from django import forms
from contratos.models import Contrato

class FormEntrar(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, max_length=8)


class FormCadastroContrato(forms.Form):
    numero_contrato = forms.CharField()
    valor = forms.CharField()
    descricao = forms.CharField()
    data_inicio = forms.DateField()
    data_fim = forms.DateField()
    tipo = forms.CharField()
    status = forms.CharField()
    arquivo = forms.FileField()


class FormEditarContrato(forms.Form):
    numero_contrato = forms.CharField()
    valor = forms.CharField()
    descricao = forms.CharField()
    data_inicio = forms.DateField()
    data_fim = forms.DateField()
    tipo = forms.CharField()
    status = forms.CharField()
    arquivo = forms.FileField(required=False)
    motivo_cancelamento = forms.CharField(required=False)
