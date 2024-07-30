import os
import requests

mensagem = 'Essa é uma menssagem!'

resposta = requests.get(
    url='http://api.textmebot.com/send.php',
    params={
        'recipiente': os.getenv('Numero do celular'),
        'text': mensagem,
        'apikey': os.getenv('API_KEY'),
    }
)
if resposta.status_code == 200:
    print('Mensagem enviada com sucesso !')