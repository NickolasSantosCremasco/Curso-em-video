print('-='*20)
print('Analisador de triângulos')
print('-='*20)

t1 = float(input('Primeiro segmento: '))
t2 = float(input('Segundo segmento: '))
t3 = float(input('Terceiro segmento: '))

if t1< t2+t3 and t2 < t1+t3 and t3 < t1 + t2:
    print('É um triangulo')
else:
    print(' Não é um triângulo')
