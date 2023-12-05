listagem = ('Lápis', 3.70,
            'Lapiseira', 5.00,
            'Borracha', 1.00,
            'Estojo', 10.00,
            'Mochila', 79.99,
            'Pochete', 1999.99)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)
