print('Gerador de PA')
termo = int(input('Digite o termo inicial: '))
razao = int(input('Digite a razao: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA: ')
    mais = int(input('\nDigite se quantos termos quer ver mais? '))
print('O programa calculou {} vezes'.format(total))
print('FIM')