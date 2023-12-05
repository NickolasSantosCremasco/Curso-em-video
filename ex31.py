distancia = int(input('Digite a distancia que quer percorrer'))
if distancia >= 200:
    valor1 = distancia*0.45
    print('o Valor da sua viagem é de {:.2f}'.format(valor1))
else:
    valor1 = distancia*0.50
    print('O valor da sua viagem é de {:.2f}'.format(valor1))
