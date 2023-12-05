from random import choice
import time
user = int(input('Escolha um numero de 0 a 5\n').strip())
numeros = [1,2,3,4,5]
escolha = choice(numeros)
if user == '':
    print('Digite algo para começar')
else:
    print('Calculando...')
    time.sleep(3)
    if user == escolha:
        print('Parabens você acertou!')
    else:
        print('Errou em... Que droga, tente mais uma vez')



