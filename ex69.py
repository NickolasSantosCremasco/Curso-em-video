masc = 0
fem = 0
menor = 0


while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: ').strip())
    sexo = str(input('Sexo [F/M]: ').strip().upper()[0])
    continuar = str(input('Quer continuar[S/N]: ').strip().upper()[0])
    if sexo not in 'FM' or continuar not in 'SN':
        print('Dados digitados incorretamente! Digite novamente')
    if sexo in 'F':
        fem += 1
        if idade <= 20:
            menor += 1
    if sexo in 'M':
        masc += 1

    if continuar in 'N':
        break
pessoas = fem + masc
if pessoas == 0:
    print('Não foi digitada nenhuma pessoa')
if pessoas == 1:
    print(f'''Foi Cadastrada 1 pessoa: 
    Nome: {nome}
    Idade: {idade}
    Sexo: {sexo}''')
if pessoas > 1:
    if fem > 1 and masc > 1:
        print(f'Foram cadastradas {pessoas} pessoas sendo {masc} Masculinos e {fem} Femininos com {menor} mulheres abaixo de 20 anos ')

    if fem > 1 and masc == 1:
        print(f'Foram cadastradas {pessoas} pessoas sendo {masc} Masculino e {fem} Femininos {menor} mulheres abaixo de 20 anos')
    if fem == 1 and masc > 1:
        print(f'Foram cadastradas {pessoas} pessoas sendo {masc} Masculinos e {fem} Feminino {menor} mulher abaixo de 20 anos')
    else:
        print(f'Foram cadastradas {pessoas} pessoas sendo {masc} Masculino e {fem} Feminino {menor} mulher abaixo de 20 anos')




