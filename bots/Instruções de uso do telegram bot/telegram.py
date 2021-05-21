import requests
import time
import json
import os


class TelegramBot:
    def __init__(self):
        token = '1770831486:AAHEDgzH-vnktjHJZ9EH_cvCQdl0YArfli0'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=20'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('menu', 'Menu'):
            return f'''Olá bem vindo a nossa loja, oque o tras aqui hoje?:{os.linesep}1 - Softwares{os.linesep}2 - Robôs{os.linesep}3 -Manutenções{os.linesep}4 - Outros'''
        if mensagem == '1':
            return f'''Softwares - R$2000,00{os.linesep}Confirmar pedido?(s/n)
            '''
        elif mensagem == '2':
            return f'''Robôs - R$2500,00{os.linesep}Confirmar pedido?(s/n)
            '''
        elif mensagem == '3':
            return f'''Manutenções - A combinar{os.linesep}Confirmar pedido?(s/n)'''
        elif mensagem =='4':
            return f'''Outros - 11951383971{os.linesep}Confirmar pedido?(s/n)'''
        elif mensagem.lower() in ('s', 'sim'):
            return ''' Pedido Confirmado! '''
        elif mensagem.lower() in ('n', 'não'):
            return ''' Desculpe por não atender as suas necessidades agora, esperamos velo aqui em breve!! :) '''
        else:
            return 'Gostaria de acessar o menu? Digite "menu"'

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()