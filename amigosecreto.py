from random import choice
from time import sleep
#Créditos a Fernando da Silva Costa Júnior

def Amigosecreto():
    escolha = int(input('''Bem-vindo, o que você deseja fazer?\n
    [1]-Adicionar participantesn\n
    [2]-Retirar participantes\n
    [3]-Ver participantes\n
    [4]-Sortear participantes\n
    [5]-Sair'''))

    if escolha == 1:
        print()

    elif escolha == 2:
        print()

    elif escolha == 3:
        print()

    elif escolha == 4:
        print()

    elif escolha == 5:
        print()

    else:
        print('ERRO escolha não encontrada.')
        sleep(1.25)
        Amigosecreto()

