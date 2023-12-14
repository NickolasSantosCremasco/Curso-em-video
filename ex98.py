from time import sleep
def contador(i,f,p):
    if p < 0:
        p*= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' - ', flush=True) #O flush serve para em vez do sleep fazer o programa
            sleep(.5)                               # esperar e rodar de uma vez ele vai voltar a rodar um por um
            cont += 1

        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' - ', flush=True)
            sleep(.5)
            cont -= p

        print('FIM')


contador(1, 10, 1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)