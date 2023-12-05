# Solicitar ao usuário que insira cinco valores
lista = []
for i in range(5):
    while True:
        try:
            valor = int(input(f'Digite um valor {i}: '))
            lista.append(valor)
            break
        except ValueError:
            print('Por favor, digite um valor numérico.')

# Exibir os valores digitados
print('-=' * 30)
print(f'Você digitou os valores {lista}')

# Encontrar o maior valor e suas posições
maior_valor = max(lista)
posicoes_maior = [i for i, valor in enumerate(lista) if valor == maior_valor]

# Encontrar o menor valor e suas posições
menor_valor = min(lista)
posicoes_menor = [i for i, valor in enumerate(lista) if valor == menor_valor]

# Exibir resultados
print(f'O maior valor digitado foi {maior_valor} nas posições {posicoes_maior}')
print(f'O menor valor digitado foi {menor_valor} nas posições {posicoes_menor}')

#Faltou apenas o fim
