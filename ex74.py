from random import choice
cont = 1
menor = 0
maior = 0
print('Os numeros que sairam no sorteio foram: ',end='')
while cont <= 5:
    sorteio = (1,2,3,4,5,6,7,8,9,10)
    sortear = choice(sorteio)
    cont+= 1
    print(sortear, end=' ')
    if sortear == 10:
        menor = sortear
        maior = sortear
    else:
        if sortear < menor:
            menor = sortear
        if sortear > maior:
            maior = sortear




print(f'\nO maior valor foi {maior}')
print(f'O menor valor foi {menor}')

#GUANABARA

from random import randint

numeros = (randint(1,10), randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'\n Os valores sorteados foram: ',end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
