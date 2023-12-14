#Ler nome e peso e armazenar em uma lista
#Mostrar:
#Quantas pessoas foram cadastradas
#Pessoas mais pesadas
#Listagem com pessoas mais leves

lista = list()
dado = list()
pesados = []
leves = []
mai = men = 0
while True:
    dado.append(str(input('Nome: '))) #temp na posição 0 é nome
    dado.append((int(input('Peso: ')))) #temp na posição 1 é o peso
    if len(lista) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    lista.append(dado[:])
    if dado[1] >= 80:
        pesados.append(dado[:])
    else:
        leves.append(dado[:])
    dado.clear()
    continuar = str(input('Quer continuar [S/N]: ').strip().upper()[0])
    while continuar not in 'SN' :
        continuar = str(input('Digite corretamente [S/N]: ').strip().upper()[0])
    if continuar in 'N':
        break

print(f'Foram registradas {len(lista)} pessoas')

print(f'o maior peso foi {mai}, as pessoas mais pesadas foram: ',end='')
for pesopesado in pesados:
    print(f'{pesopesado[0]}',end=' ')

print('\n-'*30)
print(f'O menor peso foi {men}, as pessoas mais leves foram: ', end='')
for pesopena in leves:
    print(f'{pesopena[0]}',end=' ')

