#ESTRUTURAS COMPOSTAS
#DICIONARIOS
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
#PARA TRANFORMAR OS INDICES EM INDICES LITERAIS
dados = dict() #Criando um dicionario

dados = {'nome':'Pedro','idade':25} #utilização de chaves

print(dados['nome']) #Em vez de digitar o indice agora pode digitar o nome do indice

dados['sexo'] = 'M' #Também é possivel adicionar novos indices com nomes automaticamente sem precisar digitar acima

print(dados['sexo']) #Mostrando o indice novo criado automaticamente

del dados['idade'] #Aqui eu exclui o dicionario idade

print(dados)

filme = {
    'titulo':'Star-Wars',
    'ano':1977
}

filme['diretor'] = 'George Lucas'

print(filme['titulo'])

print(filme.values()) #Vai mostrar os valores, vai retirar as keys e mostrar apenas o valor interno dela no momento

print(filme.keys()) #Vai mostrar as chaves

print(filme.items()) #Vai mostrar as duas coisas as chaves e o valor delas

for key, value in filme.items():
    print(f'{key} é {value}')

#PROGRAMAR É MUITO LEGAL CACETA

locadora = []
locadora.append(filme)
print(locadora[0]['titulo'])

#PARTE PRÁTICA

pessoas = {'nome':'Nickolas', 'sexo':'M', 'idade':17}
print(pessoas)
print(pessoas['nome']) #Agora os indices não podem conter números agora devem ser apenas o nome dos dicionarios
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos') #Lembrar de usar as aspas duplas se não da erro

print(pessoas.keys())

print(pessoas.values())

print(pessoas.items())

del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98
for k in pessoas.keys():
    print(f'{k} essas são apenas as chaves')
for v in pessoas.values():
    print(f'{v} esses são apenas os valores das chaves')
for k, v in pessoas.items():
    print(f'{k} essas são as chaves {v} esses são os valores ')

#CRIANDO DICIONARIO DENTRO DE UMA LISTA

brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) #Esse é um metodo interno para copiar itens de um dicionario para dentro de uma lista, é igual o fatiamento
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.', end='')
    print()

#PARA COLOCAR NUMEROS PEGOS EM DICIONARIOS EM ORDEM CRESCENTE BASTA FAZER
from operator import itemgetter

