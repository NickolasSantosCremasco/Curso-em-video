from utilidadesCeV import moeda

p = float(input('Digite o preco: R$ '))
disc = str(input('Digite o valor do desconto (0% a 100%): '))
aum = str(input('Digite o valor do aumento (0% a 100%): '))

moeda.resumo(p,aum,disc)