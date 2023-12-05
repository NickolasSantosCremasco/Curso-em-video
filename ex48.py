
#Revisar
soma = 0
cont = 0
for x in range(1,501,2):
    if x % 3 == 0:
        cont += 1
        soma += x
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))