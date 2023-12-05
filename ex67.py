#Mostrar a tabuada de um numero
#Perguntar se quiser ver mais tabuadas
#se não quiser basta digitar um valor menor que 0 para encerrar
#se sim mostrar a tabuada do proximo numero digitado
#no fim mostrar a mesma mensagem se quiser ou não continuar

while True:
    num = int(input('Digite um numero para ver sua tabuada: '))
    if num < 0:
        break
    for x in range(1,11):
        print(f'{num} X {x} = {num*x}')
print('FIM')

