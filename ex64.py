nove = 0
cont = 0
soma = 0
while nove != 999:
    nove = int(input('Digite [999] para parar o programa: '))
    if nove != 999:
        cont += 1
        soma += nove
print('Foram feitas {} execuções e a soma delas foi {}'.format(cont, soma))
