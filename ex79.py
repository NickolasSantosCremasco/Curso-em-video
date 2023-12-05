valores = []
continuar = str(input('Quer iniciar o programa? [S/N]: ').strip().upper()[0])
while continuar not in 'SN':
    continuar = str(input('Digite corretamente [S/N]: ').strip().upper()[0])
while continuar in 'S':
    valor = int(input('Digite um valor: ').strip())
    if valor not in valores:
        valores.append(valor)
        print('Valor registrado com sucesso! ')
    else:
        print('Valor registrado anteriormente. ')
    continuar = str(input('Quer continuar? [S/N]: ').strip().upper()[0])
    while continuar not in 'SN':
        continuar = str(input('Digite corretamente [S/N]: ').strip().upper()[0])
valores.sort()
print(f'Os valores registrados foram: {", ".join(map(str, valores))}') # O map serve para definir que elementos numéricos virem strings
