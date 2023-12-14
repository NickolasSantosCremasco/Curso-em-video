def escreve(msg):
    tam = len(msg)+4
    print('~'*tam)
    print(f'  {msg}')
    print('~' * tam)

#Programa principal
incrivel =str(input('Escreva alguma coisa: '))
escreve(incrivel)