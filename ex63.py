print('Digite quantos termos quer ver da sequencia de FIBONACCI')
termos = int(input('Quantidade: '))
cont = 1
t1 = 0
t2 = 1
while cont <= termos:
    t3 = t1 + t2
    print('{}'.format(t1), end=' ')
    t1 = t2
    t2 = t3
    cont+=1
print('FIM')