
dicionario = dict()
def notas(*num,sit=False):
    '''
    -> Função que analisa notas e a situação de alunos
    :param num: recebe uma ou mais notas de alunos da classe
    :param sit: valor opcional, indicando se deve ou não adicionar a situação do aluno
    :return: Dicionário com as informações sobre a situação da turma ou aluno
    '''
    maior = 0
    menor =0
    soma = 0

    dicionario['total'] = len(num)
    for x in num:
        if x == num[0]:
            menor = maior = x
        else:
            if x > maior:
                maior = x
            if x < menor:
                menor = x

    dicionario['maior'] = maior
    dicionario['menor'] = menor
    for x in num:
        soma += x
    media = soma/len(num)
    dicionario['média'] = media
    if sit:
        if media == 6 or media == 7:
            dicionario['situação'] = 'RAZOÁVEL'
        if media < 6:
            dicionario['situação'] = 'RUIM'
        else:
            dicionario['situação'] = 'BOA :)'




    return dicionario



#Programa Principal
rep = notas(5.5,2.5,10, sit=True)
print(rep)

