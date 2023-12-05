print('Digite sua idade para verificar seu alistamento')
idade = int(input('Idade: '))
if idade < 18:
    tempo = 18 - idade
    if tempo == 1:
        print('Falta 1 ano para seu alistamento')
    else:
        print('Faltam {} anos para seu alistamento'.format(tempo))
elif idade == 18:
    print('já é hora de se alistar ')
else:
    tempo = idade - 18
    if tempo == 1:
        print('Faz 1 ano desde seu alistamento')
    else:
        print('Fazem {} anos desde seu alistamento'.format(tempo))



