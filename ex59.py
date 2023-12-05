#Ler 2 valores
#mostrar um menu
#1 para somar
#2 para multiplicar
#3 para achar o maior
#4 para novos números
#5 para sair do programa
from time import sleep
programa = 0
num1 = float(input('Digite o primeiro valor: ').strip())
num2 = float(input('Digite o segundo valor: ').strip())

while programa != 5:


    print('''
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos Números
    [5] - Sair do programa
    ''')
    programa = int(input('Digite o valor correspondente ao seu objetivo: '))
    if programa == '' or programa > 5:
        print('Digite um valor correto ou 5 para encerrar')
        sleep(1)
    else:
        if programa == 1:
            soma = num1 + num2
            print('A soma de {} e {} é igual a {}'.format(num1, num2,soma))
            sleep(1)
        elif programa == 2:
            multi = num1*num2
            print('A multiplicação de {} e {} é igual a {}'.format(num1, num2, multi))
            sleep(1)
        elif programa == 3:
            if num1 == num2:
                print('Os dois tem o mesmo valor {}'.format(num1))
                sleep(1)
            if num1 > num2:
                print('{} é MAIOR que {}'.format(num1, num2))
                sleep(1)
            if num2 > num1:
                print('{} é MAIOR que {}'.format(num2, num1))
                sleep(1)
        elif programa == 4:
            print('Digite outros valores: ')
            num1 = float(input('1° Valor: '))
            num2 = float(input('2° Valor: '))

print('Programa Finalizado com sucesso')



