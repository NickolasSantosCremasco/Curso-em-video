#Curso de python aula 21
#interactive help
#docstrings
#argumentos opcionais
#escopa de variáveis
#retorno de resultados

#INTERACTIVE HELP ou AJUDA INTERATIVA
help()
#É so digitar no prompt de comando do python w digitar que comando você quer sabe4
help(print)
print(input.__doc__)

#Docstrings

def contador(i,f,p):
    '''
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    '''
    c = i
    while c <=f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')
contador(2,10,2)

#Se quiser saber como funciona uma função que não é do pyton e sim do código as docstrings são essenciais
help(contador) #Isso não será muito util sem antes passar a explicação dentro da função do passo a passo do que ela faz dentro0
# do programa

#PARÂMETROS OPCIONAIS
def somar(a=0,b=0,c=0): #c apartir de agora terá valor 0 se não receber nenhum valor
    s = a+b+c
    print(f'A soma vale{s}')
somar(3,2,5)
#mas e se na função somar tiver uma variavel a menos
somar(3,5)
#basta colocar o que c vai valer caso ele não for imformado

#ESCOPO DE VARIÁVEIS
#onde uma variavel vai existir e onde ela não vai mais existir

def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#Programa Principal
n = 2
print(f'No programa princiapl, n vale {n}') #n funciona pois é uma variavel globar
print(f'No programa principal, x vale {x}')#x não funciona pois é uma variavel local, funciona apenas na função



def teste2(b):
    global a # eu tambêm posso fazer um GLOBAL A que pegara a variavel criada dentro da função e tranformara em variavel global substituindo a do programa pricipal
    a = 8 #mas eu posso tambêm criar o a de dentro, a partir de agora tenho 2 variaveis com o mesmo nome mas que transmitem dados diferentes
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
#o escopo funciona da maneira que, dentro de uma função as variaveis criandas lá so funcionarão lá
teste2(a)
print(f'A fora vale {a}')
print(f'B fora vale {b}')
print(f'C fora vele {c}')
#as variaveis criadas fora da função funcionarão em todos os lugares pois são variaveis globais
#As variaveis c e b não funcionam pois foram criadas dentro de uma função então não existem no programa principal


#RETORNO DE VALORES
def somar(a=0,b=0,c=0):
    s = a+b+c
    print(f'A soma vale {s}')
somar(3,2,5)
somar(2,2)
somar(8)

#A maneira a cima não me deixa fazer prints formatados, apenas permite que eu mostre o print ja feito dentro da função, outra forma é utilizando o return

def somar(a=0,b=0,c=0):
    s = a+b+c
    return s
r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(8)

print(f'Os valores {r1}, {r2} e {r3} São resultados das somas')
#Dessa forma ela apenas vai te mandar o resultado e não vai escrever da forma que ela quiser


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')




















