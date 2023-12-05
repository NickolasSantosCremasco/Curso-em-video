#PROGRAMA DE PAR OU IMPAR
#pegar o numero digitado
#ver se quer par ou impar
#fazer o computador escolher um número aleatorio
#programa interrompido o usuario perder
#total de vitórias consecutivas
from random import choice
print('Digite para jogar par ou impar')
cont = 0
while True:
    num = int(input('Digite um número: ').strip())
    escolha = str(input('Escolha Par ou Ímpar [P/I]: ').strip().upper()[0])
    if escolha not in 'PI':
          print('Digite dados válidos')

          continue
    else:
        cpu = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        cpu = choice(cpu)
        soma = cpu + num
        parimp = soma % 2
        if parimp == 0 and escolha == 'P':
            cont += 1
            print('Parabens você acertou')
        elif parimp != 0 and escolha == 'I':
            cont+= 1
            print('Parabens você acertou')
        elif parimp == 0 and escolha != 'P':
            print('Você errou! ')
            break
        elif parimp != 0 and escolha == 'P':
            print('Você errou! ')
            break
if cont == 0:
    print('Você Não acertou nenhuma vez')
if cont == 1:
    print('Você acertou 1 apenas')
if cont > 1:
    print(f'Você acertou {cont} seguidas')

