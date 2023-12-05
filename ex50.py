soma = 0
cont = 0
for pares in range (1,7):
    num = int(input('Digite {} numero: '.format(pares)))
    if num % 2 == 0:
        soma += num
        cont += 1

print('Você informou {} números e a soma foi {}'.format(cont, soma) )
