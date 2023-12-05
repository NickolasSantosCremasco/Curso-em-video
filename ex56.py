soma = 0
menor = 0
maiorIdadeHomem = 0
nomevelho = ''
for x in range(1,5):
    print('===== {}ª PESSOA ====='.format(x))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: ').strip())
    sexo = str(input('Sexo [M/F]: ').strip().upper())
    soma += idade
    media = soma / 4
    if sexo == 'M' and x == 1:
        maiorIdadeHomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        menor += 1


print('A media de idade do grupo é {}'.format(media))
print('O homem mais velho do grupo tem {} anos e se chama {}'.format(maiorIdadeHomem, nomevelho))
print('Existem {} mulheres menores de 20 anos'.format(menor))

