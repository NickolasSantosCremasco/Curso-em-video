
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('Sua média é de {:.1f}'.format(media))
if media <= 6:
    print('Você pode ser melhor em....;)')
else:
    print('Boa mandou bem :D')