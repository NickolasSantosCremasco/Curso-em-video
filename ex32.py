from datetime import date
print('Digite um ano que falaremos se é bissexto. Ou coloque 0 para ver o ano atual.')
ano = int(input('Digite aqui: '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
