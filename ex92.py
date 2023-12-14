from datetime import date
dicionario = {'nome':str(input('Nome: ')),
              'nasc':int(input('Ano de Nascimento: ')),
              'trabalho':str(input('Digite sua carteira de trabalho (0 não tem): '))}
ano = date.today().year
idade = ano - dicionario['nasc']

if dicionario['trabalho'] == '0':
    print('-='*30)
    print(f' - Nome: {dicionario["nome"]}\n '
          f'- Idade: {idade}\n '
          f'- Carteira de trabalho: Não tem! ')
else:
    dicionario['contrato'] = int(input('Ano de contratação: '))
    dicionario['salario'] = float(input('Salário: R$ '))
    aposentadoria = 70 - idade

    print(f'-='*30)
    print(f'- Nome: {dicionario["nome"]}\n'
          f'- Idade: {idade}\n'
          f'- Carteira de trabalho: {dicionario["contrato"]}\n'
          f'- Salário: {dicionario["salario"]:.2f}')
    if idade > 70:
        dicionario['aposentadoria'] = print(f'Você se aposentou há {aposentadoria} anos.')
    else:
        print(f'- Faltam {aposentadoria} para você se aposentar')
    print('<<< FIM >>>')


