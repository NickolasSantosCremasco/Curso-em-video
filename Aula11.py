print('\033[7;37mCores no Python\033[m')

a = 4
b = 5
print('Os valores são \033[31m{}\033[m e \033[31m{}'.format(a, b))

nome = 'Nickolas'
cores = {'limpa':'\033[m', 'azul':'\033[34m','amarelo':'\033[33m'}
print('Ola {}{}{}!!!!!!'.format('\033[4;33m', nome ,'\033[m') )
print('{}{}{}'.format(cores['limpa'],nome,cores['azul']))