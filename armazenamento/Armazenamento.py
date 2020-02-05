
def menu():

    logo = '''/ \   _ __ _ __ ___   __ _ _______ _ __ ___  
             / _ \ | '__| '_ ` _ \ / _` |_  / _ \ '_ ` _ \ 
            / ___ \| |  | | | | | | (_| |/ /  __/ | | | | |
           /_/   \_\_|  |_| |_| |_|\__,_/___\___|_| |_| |_|

                / \  | |_ __ ___   ___(_) __| | __ _ 
               / _ \ | | '_ ` _ \ / _ \ |/ _` |/ _` |
              / ___ \| | | | | | |  __/ | (_| | (_| |
             /_/   \_\_|_| |_| |_|\___|_|\__,_|\__,_|'''

    print(logo)




def adicionarEstoque(idGarrafa, conteudo, engarafado):
    arquivo = open('estoque.bms', 'a+')
    conteudo = "{}|{}|{}\n".format(idGarrafa, conteudo, engarafado)

    #verificar se garafa ja existe no estoque
    '''texto = arquivo.readlines()

    for i in texto:
        local = texto.index(i)
        print(local)'''

    arquivo.write(conteudo)
    arquivo.close()



menu()


item = int(input("Digite o Número da Garrafa:"))
conteudo = input("Digite o conteúdo da Garrafa:")
engarafado = input("Digite a data do Engarafamento:")

adicionarEstoque(item, conteudo, engarafado)












