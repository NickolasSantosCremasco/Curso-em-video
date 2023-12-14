from random import randint
import time

print('DADO VIRTUAL')
print('Valores sorteados')
time.sleep(.5)
jogadores = list()
for x in range(0,4):
    valor = randint(1,6)
    jogador = {'jogo':valor}
    jogadores.append(jogador.copy())
    jogador.clear()
for x, j in enumerate(jogadores, start=1):
   print(f'O jogador {x} tirou: {j["jogo"]}')
   time.sleep(1)


