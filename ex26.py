frase = str(input('Digite alguma frase: ')).strip().upper()
print('Existem {} letras As na sua frase'.format(frase.count('A')))#aqui ele contará quantas letras as existem
print('A primeira letra A aparece na {}'.format(frase.find('A')+1))#Aqui ele achara da esquerda para direita a primeira letra A
print('A ultima letra A apareceu na {}'.format(frase.rfind('A')+1))#Aqui ele achara da direita para a esquerda a ultima letra A