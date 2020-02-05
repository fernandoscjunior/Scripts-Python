#importando blibioteca mysql para python 3.7
import pymysql

#conectando ao banco de dados Mysql
db = pymysql.connect("localhost","root","141200","juninho")

#retornando cursor da conexão
cursor = db.cursor()

######################################################################
#   INSERINDO NA TABLE NO MYSQL                                      #
######################################################################

cursor.execute("INSERT INTO usuario (id, nome) VALUES (65, 'José Carlos ')")

db.commit()

######################################################################
#   CONSULTANDO TABLE NO MYSQL                                       #
######################################################################

#realizando consulta a tabela do Mysql
cursor.execute("SELECT id, nome FROM usuario")

#retornando os registros
results = cursor.fetchall()

#varrendo os registros e imprimindo
for row in results:
    id  = row[0]
    nome = row[1]
    print ("id=%d,nome=%s" % (id, nome))

######################################################################
#   Elminando Informacao do Table                                    #
######################################################################

cursor = db.cursor()

cursor.execute("DELETE FROM usuario WHERE id = '%d'" % (123))

db.commit()

######################################################################
#    ATUALIZANDO INFORMACOES DO MYSQL                                #
######################################################################

cursor = db.cursor()

cursor.execute("UPDATE usuario SET id = id + 1 WHERE nome = '%s'"  %('José Carlos'))

db.commit()

#COMO APAGAR A TELA.
import os
def cls():
   os.system(['clear','cls'][os.name == 'nt'])

db.close()
