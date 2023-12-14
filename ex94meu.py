nomes = list()
sexos = list()
idades = list()
pessoas = dict()
while True:
    nomes.append( str(input('Nome: ').strip().capitalize()))
    sexo = str(input('Sexo [M/F]: ').strip().upper()[0])
    while sexo not in 'MF':
        print('ERRO! Por favor, Digite novamente.')
        sexo = int(input('Sexo [M/F]: '))
    sexos.append(sexo)
    idades.append( int(input('Idade: ').strip()))
    pessoas['nomes'] = nomes[:]
    pessoas['sexo'] = sexos[:]
    pessoas['idades'] = idades[:]
    continuar = str(input('Quer continuar? [S/N]: ').strip().upper()[0])
    while continuar not in 'SN':
        cotinuar = str(input('ERRO! Digite se quer continuar? [S/N]: '))
    if continuar in 'N':
        break

print(f'A) Temos {len(pessoas["nomes"])} Pessoas Cadastradas')

mediaidade = sum(pessoas["idades"]) / len(pessoas["idades"])
print(f'B) A media das idades é {mediaidade:.2f} anos')

print(f'C) As mulheres cadastradas foram: ',end='')
mulheres = []
for k,x in enumerate(sexos):
    if x == 'F':
        mulheres.append(k)
for x in mulheres:
    print(pessoas['nomes'][x], end=' ')

print(f'\nD) Listas de pessoas que estão acima da média de idades: ')

acima_media = list()
for i, x in enumerate(idades):
    if x > mediaidade:
        acima_media.append(i)
for x in acima_media:
    print(f'- Nome = {pessoas["nomes"][x]}; sexo = {pessoas["sexo"][x]}; idade = {pessoas["idades"][x]}')

print('<< ENCERRADO >>')
