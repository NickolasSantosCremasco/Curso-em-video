print('Gerador de PA')
cont = 1    #vai contar quantos termos foram
termo = int(input('Digite o início: '))
razao = int(input('Digite o fim da PA: '))
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo) , end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('\nQuantos Termos você quer mostrar mais? '))
print('Progessão finalizada com {} termos sendo mostrados'.format(total))
print('FIM')


