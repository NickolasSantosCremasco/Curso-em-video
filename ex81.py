lista  = []
continuar = str(input('Digite para iniciar o programa [S/N]: ').strip().upper()[0])
while continuar not in 'SN':
    continuar = str(input('Digite corretamente [S/N]: ').strip().upper()[0])
while continuar in 'S':
    valor = int(input('Digite um numero: '))
    lista.append(valor)
    continuar = str(input('Quer continuar [S/N]: ').strip().upper()[0])
    while continuar not in 'SN':
        continuar = str(input('Digite corretamente [S/N]: ').strip().upper()[0])
print(f'Foram digitados {len(lista)} numeros.')
lista.sort(reverse=True)
print(f'Ordenados de forma decrescente fica: {lista}')
cinco = lista.count(5)
if cinco < 1:
    print('Não foi encontrado nenhum 5')
if cinco == 1:
    print(f'Aparecereu 1 cinco ')
if cinco > 1:
    print(f'Apareceram {cinco} numeros 5')

