
#entre 18.5 a 24.9 média idea se abaixo de 17 muito abaixo do peso entre 17 e 18.49 abaixo do peso entre entre 25 a 29.99 acima do peso de 30 até 34.9 obesidade 1 entre 35 e 39.99 obesidade 2 sereva acima do 40 obesidade 3 morbida
#peso dividido pela altura

def calcularIMC(peso, altura):
    alturadois = altura * altura
    resultado = (peso / alturadois)

    if resultado < 17:
        print (f'Seu resultado é {resultado:2f} você está MUITO abaixo do peso.')
    elif resultado >= 17 and resultado <= 18.49:
        print(f'Seu resultado é {resultado:2f} você está ABAIXO do peso.')
    elif resultado >= 18.5 and resultado <= 24.99:
        print(f'Seu resultado é {resultado:2f} você está NA média.')
    elif resultado >= 25 and resultado <= 29.99:
        print(f'Seu resultado é {resultado:2f} você está ACIMA do peso.')
    elif resultado >= 30 and resultado >= 34.99:
        print(f'Seu resultado é {resultado:2f} você está com OBESIDADE LEVE.')
    elif resultado >= 35 and resultado <= 39.99:
        print(f'Seu resultado é {resultado:2f} você está com OBESIDADE SEVERA.')
    else:
        print(f'Seu resultado é {resultado:2f} você está com OBESIDADE MORBIDA.')

altura = float(input('Digite sua altura:'))
peso = float(input('Digite seu peso:'))

calcularIMC(peso, altura)

#Créditos a Fernando da Silva Costa Júnior

#teste unitario
#teste = [[13,'Seu resultado é 13 você está MUITO abaixo do peso.'],
         #[123, 'weyudfeoiwn'],
         #[780623487234,'jiuhefriuerf']]

#for valor in teste:
    #if calcularIMC(55, 1.61) == teste[1]:
       # print('true')
    #else:
        #print('false')