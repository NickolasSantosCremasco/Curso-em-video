#MODULARIZAÇÃO
#Surgiu na década de 60
#Sistema fincando cada vez maiores
#Foco:dividir um programa grande
#Foco:aumentar a legibilidade
#Foco:Facilitar a manuteção

import AULA22LinksEmPython
from AULA22LinksEmPython import dobro,triplo
#Construindo os próprios módulos
num = int(input('Digite um valor: '))
fat = AULA22LinksEmPython.fatorial(num)
print(f'O fatorial de {num} é {fat}.  ')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')

#Organização do código
#Facilidade na manutenção
#Ocultação de código detalhado
#RReutilização de código

#PACOTE
#Após você criar uma pagina apenas com as funções uma hora ou outra essa pagina tambêm ficará sobrecarregada
#com tantas funções por isso foram criados os PACOTES que separam por assuntos dentro do modulo que você ja
#criou antes