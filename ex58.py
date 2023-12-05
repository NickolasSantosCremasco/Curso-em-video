from random import choice
import time
#MELHORANDO EX28    
user = int(input('Escolha um numero de 0 a 10\n').strip())
numeros = [1,2,3,4,5,6,7,8,9,10]
escolha = choice(numeros)
tentativas = 0
if user == '':
    print('Digite algo para começar')
else:

    print('Calculando...')
    time.sleep(1)
    while user != escolha:
        user = int(input('Você errou era {}, digite novamente: '.format(escolha)))
        escolha = choice(numeros)
        print('Calculando...')
        time.sleep(1)
        tentativas += 1
if tentativas == 1:
    print('Você acertou em 1 tentativa')
else:
    print('Você acertou em {} tentativas'.format(tentativas))


