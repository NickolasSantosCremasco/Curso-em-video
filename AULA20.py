#Trabalhando com funções
def traco():
    print('-'*30)
traco()
print(f'{"Bom dia"}')
traco()
print('Nickolas')
traco()
print('Como vai? ')
traco()


#UTILIZANDO OS PARÂMETROS
#É muito interessante pois poupa muito trabalho, principalmente em coisas repetitivas que são feitas
def mensagem(msg):
    print('-----'*3)
    print(msg)
    print('-----'*3)
mensagem('SISTEMA DE ALUNOS') #Ele vai escrevendo as mesmas coisas a unica coisa que é mudada são os parametros e acaba por não precisar ficar repetindo print desnecessarios
mensagem('POUPA TRABALHO')

#Programa repetitivo
print('Programa repetitivo')
a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)

traco()
#Programa Principal
print('Programa com função soma')
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)
soma(b=4,a=8) #Pode tambem mudar a ordem dentro do parametro ja dado
soma(9,7)

#Empacotar parametros

#O asterisco num que poderia ser qualquer outro nome é basicamente o programa dizendo, ele vai passar um monte de paramentro joga tudo isso dentro de num que é jogo
def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')

contador(5,7,3,1,4)
contador(8,4,7)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [6, 3,  9, 1, 0, 2]
dobra(valores)
print(valores)