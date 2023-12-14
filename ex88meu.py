from random import randint
sorteio = list()
dado = list()
print('Sorteio da mega sena')
qtde = int(input('Digite quantos SEÇÕES você quer que sejam sorteadas: '))
tot = 1
while tot <= qtde:
    cont = 0
    while True:
        aleatorio = randint(1,60)
        if aleatorio not in dado:
            dado.append(aleatorio)
            cont += 1
        if cont >= 6:
            break

    dado.sort()
    sorteio.append(dado[:])
    dado.clear()
    tot += 1

from time import sleep
print(f'Sorteando {qtde} Jogos')
for x, l in enumerate(sorteio):
    print(f'Sorteio do jogo {x + 1}: {l}')
    sleep(.5)
print('JOGOS SORTEADOS BOA SORTE!')

