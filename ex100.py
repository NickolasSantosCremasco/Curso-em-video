from random import randint

def valores(a,b):
    lista = list()
    soma = 0
    for x in range(0,5):
        sorteio = randint(a,b)
        lista.append(sorteio)
    print(f'Sorteando 5 valores: ', end='')

    for k, v in enumerate(lista):
        print(f'{lista[k]}', end=' ')
    print('\nPRONTO')


    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'\nDentro dos valores sorteados: {lista}, temos a soma dos valores pares: {soma}')


print('Diigte até qual valor você que o programa randomize numeros: ')
valor1 = int(input('De: '))
valor2 = int(input('Até: '))
valores(valor1, valor2)