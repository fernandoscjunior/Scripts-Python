from time import sleep
from random import randint
print('Pedra,papel e tesoura')
escolha = int(input( '[1]-Pedra\n[2]-Papel\n[3]-Tesoura:'))

escocom = randint(0, 2)
sleep(1.25)

if escocom == 0: #Pedra
    if escolha == 1:
        print ('Empate.')
    elif escolha == 2:
        print('Você venceu.')
    elif escolha == 3:
        print ('Eu venci desta vez.')
elif escocom == 1:#Papel
    if escolha == 1:
        print('Eu venci desta vez')
    elif escolha == 2:
        print('Empate.')
    elif escolha == 3:
        print('Você venceu.')
elif escocom == 2:#Tesoura
    if escolha == 1:
        print('Você venceu.')
    elif escolha == 2:
        print('Eu venci desta vez.')
    elif escolha == 3:
        print('Empate.')
else:
    print('digite certo')