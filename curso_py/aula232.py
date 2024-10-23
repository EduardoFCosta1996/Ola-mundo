from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, menssagem):
        self.messagem = menssagem
        
    @abstractmethod
    def enviar(self): ...
               

class NotificacaoEmail(Notificacao) :
    def enviar(self):
        print('email: enviando', self.messagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self):
        print('SMS: enviando', self.messagem)

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    if notificacao_enviada:
        print('notificacao enviada')
    else:
        print('notificacao nao enviada')

notificacao_email = NotificacaoEmail('email enviado')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando sms')
notificar(notificacao_sms)