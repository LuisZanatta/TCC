from django.shortcuts import render
from django.core.mail.message import EmailMessage
from django.contrib.auth.models import User
from background_task import background
from contratos.models import Contrato
import datetime
from datetime import date


def calcular_segundos_entre_datas(datetime_1, datetime_2):
    return (datetime_2 - datetime_1).total_seconds()


def send_mail(contrato):
    enviar_email(repeat=86400)
    # enviar_email(repeat=60)

@background
def enviar_email():
    data_notify = date.today() + datetime.timedelta(days=30)
    contratos = Contrato.objects.filter(data_fim__lte=data_notify, status=1) | Contrato.objects.filter(data_fim__lte=data_notify, status=2)

    print('VERIFICANDO ENVIOS DE EMAILS...')

    for contrato in contratos:
        conteudo = 'O contrato ' + contrato.numero_contrato + " vence em " + str(contrato.data_fim)
        users = User.objects.filter(is_superuser=True)
        for user in users:
            mail = EmailMessage(
                subject='Atualização de Data de Vencimento de Contrato',
                body=conteudo,
                from_email='gcon@gmail.com',
                to=[user.email, ],
                headers={'Reply-To': 'gcon@gmail.com'}
            )
            mail.content_subtype = "html"
            try:
                mail.send()
            except Exception as e:
                print(e)
                print('deu certo')
