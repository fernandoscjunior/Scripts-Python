import requests
from time import sleep
import json


while True:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    requi = requests.get('https://api.promasters.net.br/cotacao/v1/valores?moedas=USD&alt=json', headers=headers)
    cotacao = json.loads(requi.text)


    print('-----------' 
        '----DOLAR----'
        '-------------')

    print ( 'O Dolar custa atualmente:', cotacao['valores']['USD']['valor'])

    sleep(2.1)

#API FOI DESCONTINUADA
#Créditos a Fernando da Silva Costa Júnior