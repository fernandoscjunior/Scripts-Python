from random import choice
from time import sleep

print ( 'Olá, sou um gênio chamado Cornélius,\nrespondo qualquer pergunta de sim e não.')
perg = ''
while True:
    per = input ( 'Coloque sua pergunta:')

    if per == 'quem é o criador':
        print ( 'Fernando Júnior.')

    elif per == 'qual sua comida favorita':
        print ( 'Yakissoba.')

    elif per == '':
        print ('Fale alguma coisa.')

    elif per == 'easter eggs':
        print ( 'Adorooooo.')

    elif per == 'por que você escreve tudo certinho':
        print ( 'Preso na lâmpada tive muito tempo para estudar português.')

    elif per == 'qual sua cor favorita':
        print ( 'Azul.')

    elif per == 'você sabe que é apenas um programa de pc':
        print ( 'O que é um pc?')

    elif per == 'você conhece o Capitão América':
        print ( 'Eu saquei a referência.')

    elif per == 'eu te odeio':
        print( 'Pelo o quê?')

    elif per == 'você me ama':
        print ( 'Amar é algo muito forte.')

    elif per == 'como vai a familia':
        print ( 'Bem, obrigado.')

    elif per == 'você é progamado em que linguagem':
        print ( 'Python3, por enquanto.')

    elif per == 'quem é você':
        print ( 'Cornélius, eu já não te disse?')

    elif per == 'qual o seu jogo favorito':
        print ('Puts, num sei.')

    elif per == 'olá, tudo bem':
        print ( 'Sim, tudo.')



    else:
        if per == perg:
            print ( 'Já não te respondi?')
        else:
            print ( 'Pensando...')
            sleep(1.5)
            print (choice(['Sim.','Não.','Talvez.','Sim.','Não.']))
            perg = per