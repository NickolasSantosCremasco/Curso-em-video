print('Digite um numero')
tot = 0
num = int(input('Numero: '))
for c in range(1, num+1):
    if num % c ==0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print('{}'.format(c), end=' ')
if tot == 2:
    print('\n\033[mO numero {} é primo pois só é divisivel por 1 e ele mesmo'.format(num))
else:
    print('\n\033[mo número {} foi divisível {} vezes'.format(num, tot))