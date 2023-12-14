def area(l,c):
    a = l * c
    print(f'A área de um terreno {l}X{c} é de {a}m²')

print('CONTROLE DE TERRENOS')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)