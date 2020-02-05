#SE CONECTANDO AO BANCO
#import sqlite3

#conn = sqlite3.connect('clientes.db')
#cursor = conn.cursor()
#conn.close()

#INSERINDO INFORMAÇÕES INSERIDAS PELO ÚSUARIO
#cursor.execute("""
#INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
#VALUES (?,?,?,?,?,?,?,?)
#""",# (p_nome, p_idade, p_cpf, p_email, p_fone, p_cidade, p_uf, p_criado_em))

#conn.commit()

#print('Dados inseridos com sucesso.')

#conn.close()
#ATUALIZANDO OS DADOS
#cursor.execute("""
#UPDATE clientes
#SET fone = ?, criado_em = ?
#WHERE id = ?
#""", #(novo_fone, novo_criado_em, id_cliente))

#conn.commit()

#print('Dados atualizados com sucesso.')

#conn.close()

#DELETANDO DADOS
#cursor.execute("""
#DELETE FROM clientes
#WHERE id = ?
#""", #(id_cliente,))

#conn.commit()

#print('Registro excluido com sucesso.')

#conn.close()