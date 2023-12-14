dados = list()
dados.append('Pedro')
dados.append(25)

#Criando uma lista copia da ultima
pessoas = list()
pessoas.append(dados[:])

pessoas = [['Pedro',25],['Maria',12]]

print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[1])


#Parte prática

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
teste[0] = 'Maria'
teste[1] = '22'
galera.append(teste[:])

print(galera)

galera = list()
dados = list()
totmai = 0
totmen = 0
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:]) #Se Não criar uma copia dessa maneira na hora que der o clear vai apagar todos os dados pois eles vão estar interligados e não copiados
    dados.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} É menor de idade.')
        totmen += 1
print(f'Temos {totmai} Maiores e {totmen} Menores.')