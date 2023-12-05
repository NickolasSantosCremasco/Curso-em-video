print('-='*20)
print('Analisador de triângulos')
print('-='*20)

t1 = float(input('Primeiro segmento: '))
t2 = float(input('Segundo segmento: '))
t3 = float(input('Terceiro segmento: '))

if t1< t2+t3 and t2 < t1+t3 and t3 < t1 + t2:
    if t1 == t2 == t3:
        print('É um triangulo Equilátero')
    elif t1 == t2 != t3 or  t1 == t3 != t2 or  t3 == t2 != t1:
        print('É um triangulo isósceles')
    elif t1 != t2 != t3:
        print('É um triangulo escaleno')

else:
    print(' Não é um triângulo')
