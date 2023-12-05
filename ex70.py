print('-'*20)
print('LOJA DAORA')
print('-'*20)
soma = 0
mMil = 0
cont = 0
menor = 0
while True:
    produto = str(input('Nome do Produto: ').strip())
    preco = float(input('Preço: ').strip())
    continuar = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    cont += 1
    soma += preco
    if preco >= 1000:
        mMil += 1
    if cont == 1:
        barato = produto
        menor = preco
    if cont > 1:
        if preco < menor:
            menor = preco
            barato = produto

    if continuar in 'N':
        break
print(f'''Foram digitados {cont} Produtos
Preço da compra ficou de R${soma:.2f}
O {barato} foi o produto mais barato ficando em R${menor:.2f}''')
