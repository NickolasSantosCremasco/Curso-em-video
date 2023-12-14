print('-='*5, 'DIGITE O NOME E NOTA DOS ALUNOS PARA VER SUAS MÉDIAS', '=-'*5)
alunos = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    # Armazena os dados do aluno em uma lista
    aluno = [nome, nota1, nota2]

    # Adiciona a lista do aluno à lista de alunos
    alunos.append(aluno)

    continuar = input('Quer continuar? [S/N]').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Digite corretamente [S/N]: ')
    if continuar == 'N':
        break

print('No. NOME     MÉDIA')
for i, aluno in enumerate(alunos, start=1):
    nome = aluno[0]
    media = (aluno[1]+aluno[2]) / 2
    #outra alternativa
    media = sum(aluno[1:])/2
    print(f"{i:<3} {nome:<8} {media:.2f}")