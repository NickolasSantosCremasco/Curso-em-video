print('Digite o peso de 5 pessoas')
menor = 0
maior = 0
for x in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(x)))
    if x == 1:
        maior = x
        menor = x
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {} Kg'.format(menor))
