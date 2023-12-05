num = int(input('Digite um numero entre 0 e 20: '))
numeros = ('Zero','Um','Dois','três','quatro','cinco','seis','sete','oito',' nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte' )
while num > 20 or num < 0:
    num = int(input('Dados inválidos digite um numero de 0 a 20: '))
extenso = numeros[num]
print(f'O numero escolhido foi {extenso}')
