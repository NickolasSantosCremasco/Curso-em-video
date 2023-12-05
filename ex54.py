from datetime import date
'''anoAtual = date.today().year
anoAtual -= 18
velho = 0
novo = 0
print(anoAtual)
for idade in range(1,8):
    ano = str(input('Digite o ano a {} pessoa nasceu: '.format(idade)))
    if idade <= anoAtual:
        velho += 1
    else:
        novo += 1
print('Existe {} Maiores de idade e {} Menores de idade'.format(velho,novo))'''

#NÃO FUNCIONOU

#GUANABARA

atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E {} Menores de idade'.format(totmenor))

