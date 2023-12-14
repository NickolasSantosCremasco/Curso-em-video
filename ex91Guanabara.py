from random import randint
import time
from operator import itemgetter

jogo = {'jogador1':randint(1,6),
        'jogador2':randint(1,6),
        'jogador3':randint(1,6),
        'jogador4':randint(1,6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    time.sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #Aqui ele dara o resultado em forma de lista que tem tuplas dentro
print('-='*30)
print('RANKING JOGADORES')
for i, v in enumerate(ranking, start=1):
    print(f'{i}º Lugar: {v[0]} com {v[1]}')
    time.sleep(1)
