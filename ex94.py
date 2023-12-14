galera = list()
pessoa = dict()

soma = 0
pessoa['nome'] = str(input('Nome: '))
while True:
    pessoa.clear()
    pessoa['sexo'] = str(input('Sexo: [M/F]: ').upper()[0])
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]'))
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO!, Por favor, digite apenas F ou M.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
        print()
print('<< ENCERRADO >>')