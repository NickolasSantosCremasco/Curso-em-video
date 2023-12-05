for x in range(0,5): # 1, 6 só mostra 5 vezes pula o primeiro numero
                     # 0, 6 mostra 6 vezes
    print('oi')
print('Fim')

for i in range (0,5):
    print(i)
print('FIM')

for z in range(6,0,-1): #Se quiser que conte negativamente
    print(z)
print('FIM')

for c in range(0,7,2):
    print(c)

n = int(input('Digite um número: '))
i = int(input('Digite o intervalo: '))
p = int(input('Digite o passo: '))
for c in range(n, i+1, p):
    print(c)
print('Fim')
s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi de {}'.format(s))
