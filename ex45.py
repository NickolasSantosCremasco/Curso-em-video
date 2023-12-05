import time
from random import choice
print('Digite para um dos numeros para jogar jokenpô')

print(''' 1 - Tesoura
 2 - Papel
 3 - Pedra''')
msgInicial = ['Estou me decidindo....', 'Essa ta difícil', 'Deixa eu pensar aqui... ']
msgInicial = choice(msgInicial)

jogada = int(input('Digite a jogada: '))
print('{}'.format(msgInicial))
time.sleep(1.5)
print('Pronto')
time.sleep(.5)
print('JO')
time.sleep(.5)
print('KEN')
time.sleep(.5)
print('PÔ')
time.sleep(.5)

jokenpo = [1, 2, 3]
escolha = choice(jokenpo)
if jogada == escolha:
    if jogada == 1 and escolha == 1:
        print('''Tesoura VS Tesoura''')
        time.sleep(.5)
        print('Empate!')
    elif jogada == 2 and escolha == 2:
        print('''Papel VS Papel''')
        time.sleep(.5)
        print('Empate!')
    elif jogada == 3 and escolha == 3:
        print('''Pedra VS Pedra''')
        time.sleep(.5)
        print('Empate!')
elif jogada != escolha:
    if jogada == 1 and escolha == 2:
        print('''Tesoura VS Papel!''')
        time.sleep(.5)
        print('Venceu!')
    elif jogada == 1 and escolha == 3:
        print('Tesoura VS Pedra')
        time.sleep(.5)
        print('Pedreu!')
    elif jogada == 2 and escolha == 1:
        print('''Papel VS Tesoura''')
        time.sleep(.5)
        print('Perdeu!')
    elif jogada == 2 and escolha == 3:
        print('''Papel VS Pedra''')
        time.sleep(.5)
        print('Venceu!')
    elif jogada == 3 and escolha == 1:
        print('Pedra VS Tesoura')
        time.sleep(.5)
        print('Venceu!')
    elif jogada == 3 and escolha == 2:
        print('Pedra VS Papel')
        time.sleep(.5)
        print('Perdeu!')
