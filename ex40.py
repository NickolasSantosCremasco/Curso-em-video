print('Digite sua nota trimestral')
p1 = float(input('NOTA 1: '))
p2 = float(input('NOTA 2: '))
p3 = float(input('NOTA 3: '))

media = (p1 + p2 + p3)/3

if media <5 :
    print('Puta irmão, tu ta reproved de ano meu parça')
elif media >5 and media < 6.9:
    print('Esta de recuperação em, passou triscando')
else:
    print('Para bens, tu ta vivasso agr vc evoluiu de estudante estrupado do 1 ano para estudante estrupado do 2')
