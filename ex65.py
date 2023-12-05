#Input de um número
#Perguntar se quer continuar
# se o valor de quer continuar for = n então acabar o programa
# o valor for = s continuar pegando mais números
# no final mostrar quantos numeros foram digitados
# a media entre eles
# o maior valor deles
# o menor valor deles

print('Digite um numero na sequencia numerica')
continuar = str(input('Quer Iniciar o programa[S/N]: ').strip().upper()[0])
while continuar not in 'SsNn':
    continuar = str(input('Digite novamente [S/N]: '))
cont = soma = maior = menor =0

while continuar not in 'Nn':
    num = int(input('Digite um número: '))
    continuar = str(input('Que continuar? [S/N] ').strip().upper()[0])
    while continuar not in 'SsNn':
        continuar = str(input('Digite corretamente [S/N]: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma/cont
print('Foram digitados {} numeros com uma média de {:.2f}'.format(cont, media))
print('O menor numero digitado foi {} e o maior foi {}'.format(menor, maior))
