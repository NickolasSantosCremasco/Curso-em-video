print('-='*5, 'DIGITE O NOME E NOTA DOS ALUNOS PARA VER SUAS MÉDIAS', '=-'*5)
alunos = [] #lista alunos
temporario = [] #lista temporario, para armazenar os dados e logo depois apagar para regeber novos
while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    #areas de input dos dados
    while nota1 > 10 or nota1 < 0 or nota2 > 10 or nota2< 0:
        print('Digite corretamente os dados!')
        nome = str(input('Nome: '))
        nota1 = int(input('Nota 1: '))
        nota2 = int(input('Nota 2: '))
        #Se os dados forem digitados de alguma forma errada


    temporario.append(nome)
    temporario.append(nota1)
    temporario.append(nota2)
    #Aqui a cada dado digitado ele vai adicionar na lista temporario

    alunos.append(temporario[:])
    #Aqui ele vai copiar os dados do temporario para a lista alunos que sera mostrada no fim

    temporario.clear()
    #limpara a lista temporario para ela ficar apta para outros dados

    continuar = str(input('Quer continuar? [S/N]').strip().upper()[0])
    #Aqui é continuidade do programa se o usuario digitar sim para continuar o programa executara novamente se não parará

    while continuar not in 'SN':
        continuar = str(input('Digite corretamente [S/N]: '))
        #Se o usuario digitar erroneamente os dados o programa pedira para digitar corretamente

    if continuar in 'N':
        break
        #Se o continuar for não o programa parará

print('No. NOME     MÉDIA')
#Aqui mostrara o fim, o nome e a média das notas de cada aluno que foi digitada acima

for i, aluno in enumerate(alunos):
    #Para cada aluno dentro da lista alunos faça começando enumerando pelo 1

    nome = aluno[0]
    #Criando uma variavel para ficar mais facil mostrar o nome do que fica dentro da lista na posição aluno[0]

    media = (aluno[1] + aluno[2])/2
    #Calculo da média do aluno

    print(f'{i}º {nome:>10} {media:>10}')

    #Por fim mostra o numero do aluno digitado o nome dele e a média de nota que foi contata acima
while True:
    print('-' * 30)
    num = int(input('Digite o numero do aluno que quer ver as notas [999 interrompe]: '))
    print('-' * 30)
    if num == 999:
        break
    print('-'*30)
    print(f'As notas de {alunos[num][0]} foram {alunos[num][1]} e {alunos[num][2]} ')




