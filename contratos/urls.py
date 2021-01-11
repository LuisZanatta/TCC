from django.urls import path
from contratos.views import entrar, sair, index_contratos, cadastrar_contrato, deletar_contrato, editar_contrato, detalhe_contrato

urlpatterns = [
    path('', entrar),
    path('sair/', sair),
    path('contratos/', index_contratos),
    path('contratos/criar/', cadastrar_contrato),
    path('contratos/deletar/<int:id>/', deletar_contrato),
    path('contratos/editar/<int:id>/', editar_contrato),
    path('contratos/<int:id>/', detalhe_contrato),
]
