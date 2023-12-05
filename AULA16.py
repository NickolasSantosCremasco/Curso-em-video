#3 Tipos de variáveis

#Tuplas
#Lanche = ()

#Listas
#Lanche = []

#Dicionarios
#Lanche = {}

lanche = ('Hambúrguer','Suco','Pizza','Pudim')


print(lanche[:-1]) #Sempre desconsidera o ultimo elemento


for comida in lanche:
    print(f'\033[31mEu vou comer {comida}')

for cont in range(0,len(lanche)):
    print(f'Vou comer {lanche[cont]} Na posicao {cont}')
print('\nComi pra caceta ')

#Aqui ele da o dado de lanche e a posição
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')


print(sorted(lanche)) # Coloca em ordem
a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
print(c.count(5))
print(c.index(8))# mostra em que posição esta o 8
print(c.index(2,1)) # Mostra em que posição esta o numero dois mas não começa a contar do indice 0 e sim do indice 1 para frente

pessoa = ('Nickolas', 17, 'M', 99.88)
print(pessoa)
del(pessoa) #Apaga a variavel da memória, só não pode apagar um elemento dentro de uma tupla