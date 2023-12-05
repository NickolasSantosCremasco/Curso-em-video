print('='*40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('='*40)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimoT = termo+(10)*razao
for x in range(termo, decimoT, razao):
    print(x, end=' -> ')
print('ACABOU!')