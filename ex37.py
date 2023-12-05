print('Digite um número inteiro para ter sua converção')
num = int(input('Seu número: '))
convercao = int(input('''1 - Binário
2 - Octal
3 - Hexadecimal
Sua opção:'''))
if convercao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format((num), bin(num)[2:]))
elif convercao == 2:
    print('{} convertido para OCTAL é igual a {}'.format((num), oct(num)[2:]))
elif convercao == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format((num), hex(num)[2:]))
else:
    print('Opção inválida, digite novamente! ')
