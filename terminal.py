#IMPORTANDO AS BIBLIOTECAS
from time import sleep
import os
from tkinter import *


clear = os.system('clear') 

#CONFIGURANDO A JANELA
janela = Tk()
janela.title("Terminal")
janela["bg"] = "black"


#CONFIGURANDO O INÍCIO
def aPanda():
    print('\nBem-vindo (para uma ajuda tente: help ou about')
#CONFIGURANDO O SISTEMA
def Panda():
    print('\\:')
    cod = input()
    if cod == 'show':
        print('O que deseja mostrar?')
        m = input()
        sleep(0.3)
        print(m)
        Panda()

    elif cod == 'help':
        sleep(0.3)
        print('''Comandos disponiveis:
        show (serve para mostrar algo na tela)
        help (ajuda)
        about (fala sobre o sistema)
        clear (limpa a tela)
        exit (sai do terminal)
        testwindow (ver uma janela)''')

        i = input()
        clear      
        Panda()

    elif cod == 'about':    
        print('Sistema terminal Panda. v.1.0\n(de enter para sair).')
        i = input()
        print(i)
        sleep(0.3)
        clear
        Panda()
    
    elif cod == 'clear':
        clear
        Panda()

    elif cod == 'exit':
        print('ok...')
        sleep(1.3)

    elif cod == '':
        print('')
        i = input()
        clear
        Panda()

    elif cod == 'secret':
        print('Autor: Fernando da Silva Costa Júnior.\nLínguagem: Python 3.6')    

    elif cod == 'testwindow':
        print()

    else:
        print(f'ERRO, comando:{cod} não existe, tente help.\n\n(enter para sair).')
        i = input()
        clear
        Panda()

aPanda()        
Panda()

#Créditos Fernando da Silva Costa Júnior