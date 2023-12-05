
nome = str(input('Digite seu nome completo: ')).strip().split()
print('Seu primeiro nome é {}'.format(nome[0])) #vai mostrar o primeiro nome
print('Seu ultimo nome é {}'.format(nome[len(nome)-1])) #vai mostrar o nome na posição len -1
#-1 mostra como se fosse o ultimo, 0 é o primeiro e -1 é o ultimo da direita