from django.shortcuts import render
from contratos.forms import FormEntrar
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from contratos.models import Contrato, Aditivo
from contratos.forms import FormCadastroContrato
from django.contrib import messages

def entrar(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect('/contratos/')
        return render(request, 'index.html')
    if request.method == 'POST':
        form = FormEntrar(request.POST)
        if form.is_valid():
            usuario = authenticate(request, 
                                   username=form.cleaned_data['username'], 
                                   password=form.cleaned_data['password'])
            if usuario is not None:
                login(request, usuario)
                return HttpResponseRedirect('/contratos')
    context = {
        'mensagem': 'Usuário e/ou Senha incorretos!'
    }
    return render(request, 'index.html', context)


def sair(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/')
def index_contratos(request):
    context = {
        'contratos': Contrato.objects.all(),
    }
    return render(request, 'home.html', context)


@login_required(login_url='/')
def cadastrar_contrato(request):
    if request.method == 'POST':
        form = FormCadastroContrato(request.POST, request.FILES)
        if form.is_valid():
            novo_contrato = Contrato()
            print(form.cleaned_data)
            print(form.cleaned_data['numero_contrato'])
            novo_contrato.numero_contrato = form.cleaned_data['numero_contrato']
            novo_contrato.valor = form.cleaned_data['valor']
            novo_contrato.descricao = form.cleaned_data['descricao']
            novo_contrato.data_inicio = form.cleaned_data['data_inicio']
            novo_contrato.data_fim = form.cleaned_data['data_fim']
            novo_contrato.tipo = form.cleaned_data['tipo']
            novo_contrato.status = form.cleaned_data['status']
            novo_contrato.arquivo = form.cleaned_data['arquivo']
            novo_contrato.usuario = request.user
            novo_contrato.save()
            messages.success(request, 'Contrato cadastrado com sucesso!')
            return HttpResponseRedirect('/contratos/')
        messages.error(request, 'Contrato não cadastrado! Verifique os campos e tente cadastrar novamente!')
        print(form.errors)
        return HttpResponseRedirect('/contratos/')

@login_required
def deletar_contrato(request, id):
    contrato = Contrato.objects.filter(id=id).first()
    if contrato:
        contrato.delete()
        messages.success(request, 'Contrato deletado!')
    else:
        messages.error(request, 'Contrato não encontrado!')
    return HttpResponseRedirect('/contratos/')