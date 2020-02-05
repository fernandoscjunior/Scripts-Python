import re

strteste = 'Batata é iluminate.'

variavelpadrao = re.search(r'Batat.',strteste)

#re.findall mostra todas as possibilades dentro da frase

#o . significa qualquer carctere ali pode se usar \w que tem um efeito parecido se vc usar um + depois do \w vc pega todas as letras depois do \w.
#se usar * ira pegar os 'batat' tambem tipo o + so pega os que tem as letras a mais o * nao ele pega tudo.

#o r antes das '' significa raw, raw string que deixa a string sem caractere especial

#se usa o 'raw' porque nas expressoes regulares pois muitos dos carcteres sao especiais e bugariam tudo.

print (variavelpadrao.group())

#o .group serve para mostrar p padrao da variavelpadrao
#use if para ver se acha o padrao na frase ex:if variavelpadrao:
