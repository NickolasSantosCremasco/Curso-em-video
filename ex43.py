print('Digite o peso e a altura de 6 pessoas: ')
sheip = 0
for pess in range(1,7):
    peso = float(input('Peso: '))
    alt = float(input('Altura: '))
    imc = peso / (alt**2)
    print('{:.1f}'.format(imc))
    if imc <= 25 and imc >= 18.5:
        sheip += 1
print('Dessas {} pessoas existem {} sheipadas'.format(pess, sheip))

