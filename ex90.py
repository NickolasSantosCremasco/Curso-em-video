print('DIGITE O NOME E A MÉDIA PARA VER A SITUAÇÃO DO ALUNO')
alunos = list()
nome = str(input('Nome: '))
media = float(input('Média: '))
dicionario = {'nome':nome, 'media':media}
alunos.append(dicionario.copy())
dicionario.clear()
if alunos[0]['media'] >= 7:
    print(f'o aluno: {alunos[0]["nome"]} \nEsta com média: {alunos[0]["media"]} \nPor tanto esta Aprovado')
else:
    print(f'o aluno: {alunos[0]["nome"]} \nEsta com média: {alunos[0]["media"]} \nPor tanto esta Reprovado')

