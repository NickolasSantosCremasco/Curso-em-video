print('Digite as seguintes informações para aprovarmos o empréstimo')
#Qual o valor da casa

casa = float(input('Digite o valor da casa: R$'))
#Salário

salario = float(input('Digite seu salário: R$'))
#quantos anos ele pretende pagar

tempo = int(input('Digite em quantos anos você pretende pagar: '))

#Calcular

mes = tempo*12
#valor da prestação mensal
parcelas = casa/mes
porcenSal = (salario*30)/100
#Não pode ser maior que 30% do salário

if parcelas > porcenSal:
    print('você pagara {:.2f} mensalmente durante {} anos'.format(parcelas, tempo), end='')#isso basicamente faz a mesma coisa que os ''' no print
    print('emprestimo negado')
else:
    print('Você pagará   {:.2f} mensalmente'.format(parcelas))
    print('Empréstimo CONCEDIDO')

#