#LISTAS

#Diferente das Tuplas que são imutáveis as listas são mutaveis

lanche = ['Lanche','Suco','Pizza','Pudim']
print(lanche)
lanche[3] = 'Picole'
print(lanche)

#So que nas listas você não coloca por exemplo lanche[4] = 'Picles', voce coloca o comando:

lanche.append('Arroz')
print(lanche) #Isso adiciona ao final da lista

#Se quiser adicionar no meio da lista de elementos basta usar o elemento

#Primeiro você utiliza o comando insert, define em que lugar quer inserir e depois escreve o objeto
lanche.insert(0,'Pão')
print(lanche)

#Se quiser apagar um elemento tem várias formas uma delas é o:

del lanche[3]
print(lanche) #É possivel ver que deletou dessa lista apenas o elemento Pizza

#OU

lanche.pop(3) #Tem a mesma função do del, esses eliminam o elemento e reposicionam os índices
print(lanche)

#OU

lanche.pop() #dessa forma se não tiver nenhum elemento escrito ele elimina o ultimo da direita
print(lanche)

lanche.remove('Pão') #A unica diferença desse para os outros é que ele remove pelo mnome do elemento e não pelo indice
print(lanche)

#Para remover um elemento primeiro deve verificar se ele esta na lista se não da erro no programa

if 'Lanche' in lanche:
    lanche.remove('Lanche')
print(lanche)


valores = list(range(4,11)) #Cria uma estruta ordenada nesse programa aparecerá a estrutura de 4 a 10
print(valores)

valores = [8,2,5,4,9,3,0]
valores.sort() #Esse ordena os valores do menor para o maior da esquerda para direita
print(valores)

sorted(valores) #organiza da mesma forma só que com outra tipagem

#Para ordenar na maneira inversa isso é da direita para esquerda basta escrever

valores.sort(reverse=True)
print(valores)

print(len(valores))



valores = []
valores.append(4)
valores.append(5)
valores.append(9)


for posicao, valor in enumerate(valores):
    print(f'Na posição {posicao + 1} encontrei o valor {valor}!')
print('Cheguei ao final da lista.')

valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    valores.sort(reverse=True)
for c, v in enumerate(valores):
    print(f'Na posição {c + 1} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

#Esse codigo não cria uma copia da lista e sim uma ligação entre elas, qualquer mudança feita em uma muda a outra
a = [2,3,4,5]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#Para criar uma cópia basta fazer isso:

a = [2,3,4,5]
b = a[:] #Colocar em prática as regras do fatiamento, ele copiara todos os itens da esquerda quanto os itens da direita
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

