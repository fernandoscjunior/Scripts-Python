import requests

#puxando informações
#alem do .get tem o .post que funciona de forma parecida ou none para defineir uma variavel como nada.

#para mais funçoes estude e use beautiful soup 4 pip install bs4
#isso é o que vc precisa saber para saber mais pesquise ou veja a aula 12 do curso basico de python do caveira tech



try:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    requisicao = requests.get('https://google.com',headers=headers)

#pode se usar a biblioteca json para pegar json com json.loads


#pode se usar requisiçao.text para se ver o texto inserido na pagina acima

except Exception as e:
    print ( 'Deu o erro ', e)


#para ver requisiçoes va ao site putsreq
