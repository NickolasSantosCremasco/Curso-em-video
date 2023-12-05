print('Digite uma frase para ver se é um palindromo')
frase = str(input('Frase: ')).strip().upper()
palavras = frase.split() #Identificara e separa os espaços fazendo uma lista de strings
junto = ''.join(palavras) #juntara as strigs outrora separadas mas juntara em 1 apenas
inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto)-1,-1,-1):
    # 1. Pegara o numero de letras de junto e tirara 1 por causa da contagem estranha do for
    # 2. o len negativo ou seja o primeiro da direita para esquerda
    # 3. e a partir do primeiro da direita ele ira contar as letras de traz para frente, a função sera de -1 em -1
    inverso += junto[letra] #isso não printara de 1 em 1 e sim em 1 string só'''
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada NÃO é um palíndromo')