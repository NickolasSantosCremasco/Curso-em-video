from random import randint
from time import sleep
print('-'*30)
print('       JOGA NA MEGA-SENA         ')
print('-'*30)
lista = list()
jogos = list()
qtde = int(input('Quantos jogos você quer que sejam sorteados? ').strip())
tot = 1
while tot <= qtde:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'Sorteando {qtde} Jogos', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i +1}: {l}')
    sleep(.5)
