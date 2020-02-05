
class Biblioteca:

    def __init__(self):
        self.db = pymysql.connect("localhost","root","141200","juninho")
        self.cursor = self.db.cursor()

    def add(self, livro_id):
        nomezinho = str(input('Digite o nome do livro:'))
        self.cursor.execute(f"INSERT INTO livros(nome) VALUES ('{nomezinho}')")
        db.commit()
        show()

    #def remove(self, livro_id):

    def situacao(self):
        self.cursor.execute("SELECT nome, situacao FROM livros")
        results = self.cursor.fetchall()
        for row in results:
            nome = row[0]
           situacao = row[1]
            print ("Nome do livro:\n|%s|\nEmpréstimo:\n|%s|" % (nome, situacao)) 

    def search(self, livro_id): 
        j = str(input('Digite o nome do livro que deseja procurar:'))
        jaca = self.cursor.execute(f"SELECT nome FROM livros WHERE UPPER(nome) = UPPER('{j}')")
        if jaca == 0:
            print('Livro não encontrado :( .')
            sleep(2)
            show()
        elif jaca == 1:
            self.cursor.execute(f"SELECT nome, situacao FROM livros WHERE nome = ('{j}')")
            results = self.cursor.fetchall()
            for row in results:
                nome = row[0]
                situacao = row[1]
                print('LIVRO ENCONTRADO!!!')
                print ("Nome do livro:\n|%s|\nSituação:\n|%s|" % (nome, situacao)) 

    def realizarEmprestimo(self, livro_id):
        idz = int(input('Qual o id do aluno?:'))
        c = self.cursor.execute(f"SELECT emprestimo FROM alunos Where id = ({idz})")
        db.commit
        if c == 'emprestimo em uso':
            print('Esse aluno já possui um livro.')
            show()

        else:
            livrozin = str(input('Qual livro você quer?:'))
            l = cursor.execute(f"SELECT situacao FROM livros WHERE nome =('{livrozin}')")
            if l == 'emprestado':
                print('Este livro já foi emprestado.')
                show()

            else:
                cursor.execute(f"UPDATE livros SET situacao = ('emprestado') WHERE nome = ('{livrozin}')")
                cursor.execute(f"UPDATE alunos SET emprestimo = ('emprestimo em uso') WHERE id = ({idz})")
                sleep(3)
                db.commit()
                show()

    def devolucaoEmprestimo(self, livro_id):
        al = int(input('Qual o id do aluno que irá devolver?:'))
        liv = str(input('Qual o nome do livro?:'))
        f = cursor.execute(f"SELECT emprestimo FROM alunos WHERE id = ({al})")

        if f == '':
            print('O aluno não tem livro.')

        else:
            cursor.execute(f"UPDATE alunos SET emprestimo = ('') WHERE id = ({al})")
            cursor.execute(f"UPDATE livros SET situacao = ('') where nome = ('{liv}')")
            print('Livro devolvido com sucesso.')
            db.commit()
            show()
    

 
        
        
