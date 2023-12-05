print('Digite um numero eu dizer se é par ou impar')
num = int(input('').strip())
parimp = num%2
if parimp == 0:
    print('É par')
else:
    print('É impar')