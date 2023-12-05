print('{:=^65}'.format(' LOJAS NICK-COLAS '))
print('Digite as informações do produto e informaremos o quanto deverá ser pago')
produto = input('Produto: ').strip().capitalize()
valor = float(input('Valor: ').strip())
unidades = int(input('Quantidade: ').strip())
valor = unidades*valor

print('''Digite o numero respectivo a forma de pagamento:
1 - À Vista em Dinheiro
2 - À Vista no Cartão
3 - 2x no cartão
4 - 3x ou mais no cartão''')
pagamento = int(input('Forma de pagamento: '))
if pagamento == 1:
    desconto = (valor*10)/100
    desconto = valor-desconto
    if unidades > 1 and produto[-1] not in 's': #Se as unidades forem maiores que 1 e o produto[-1] não esta em s
        plural = produto + 's' #Adiciona um s final a string se estiver no sigular mas for mais de um na quantidade
        print('Os(as) {} Custarão R${} '.format(plural, desconto))
    elif unidades == 1 and produto[-1] in 's': #Se as unidades forem iguais a 1 e o produto[-1] for igual a s
        singular = produto[:-1] #Remove o s final da string
        print('O(a) {} Custará R${}'.format(singular,desconto))
    elif unidades > 1 and produto[-1] in 's':
        print('Os(as) {} Custarão {}'.format(produto, desconto))
    else:
        print('O(a) {} Custará R${}'.format(produto,desconto))


elif pagamento == 2:
    desconto = (valor*5)/100
    desconto = valor - desconto

    if unidades > 1 and produto[-1] not in 's':  # Se as unidades forem maiores que 1 e o produto[-1] não esta em s
        plural = produto + 's'  # Adiciona um s final a string se estiver no sigular mas for mais de um na quantidade
        print('Os(as) {} Custarão R${:.2f} '.format(plural, desconto))

    elif unidades == 1 and produto[-1] in 's':  # Se as unidades forem iguais a 1 e o produto[-1] for igual a s
        singular = produto[:-1]  # Remove o s final da string
        print('O(a) {} Custará R${:.2f}'.format(singular,desconto))

    elif unidades > 1 and produto[-1] in 's':
        print('Os(as) {} Custarão R${:.2f}'.format(produto, desconto))

    else:
        print('O(a) {} Custará R${:.2f}'.format(produto, desconto))

elif pagamento == 3:
    parcelamento = valor / 2
    if unidades > 1 and produto[-1] not in 's':  # Se as unidades forem maiores que 1 e o produto[-1] não esta em s
        plural = produto + 's'  # Adiciona um s final a string se estiver no sigular mas for mais de um na quantidade
        print('Os(as) {} Custarão R${:.2f}, em 2 parcelas valerão R${:.2f}'.format(plural, valor, parcelamento))

    elif unidades == 1 and produto[-1] in 's':  # Se as unidades forem iguais a 1 e o produto[-1] for igual a s
        singular = produto[:-1]  # Remove o s final da string
        print('O(a) {} Custará R${:.2f}, em 2 parcelas valerão R${:.2f}'.format(singular,valor,parcelamento))

    elif unidades > 1 and produto[-1] in 's':
        print('Os(as) {} Custarão R${:.2f}, em 2 parcelas valerão R${:.2f}'.format(produto, valor, parcelamento))

    else:
        print('O(a) {} Custará R${:.2f}, em 2 parcelas valerão R${:.2f}'.format(produto, valor, parcelamento))

elif pagamento == 4:
    parcelamento = int(input('Serão quantas parcelas: '))
    desconto = (valor*20)/100
    juros = valor+desconto
    parcelas = juros/parcelamento

    if unidades > 1 and produto[-1] not in 's':  # Se as unidades forem maiores que 1 e o produto[-1] não esta em s
        plural = produto + 's'  # Adiciona um s final a string se estiver no sigular mas for mais de um na quantidade
        print('Os(as) {} Custarão R${:.2f} e as parcelas R${:.2f} '.format(plural, juros, parcelas))

    elif unidades == 1 and produto[-1] in 's':  # Se as unidades forem iguais a 1 e o produto[-1] for igual a s
        singular = produto[:-1]  # Remove o s final da string
        print('O(a) {} Custará R${:.2f} e as parcelas R${:.2f}'.format(singular, juros, parcelas))

    elif unidades > 1 and produto[-1] in 's':
        print('Os(as) {} Custarão R${:.2f} e as parcelas R${:.2f}'.format(produto, juros, parcelas))

    else:
        print('O(a) {} Custará {:.2f} e as parcelas R${:.2f}'.format(produto, juros, parcelas))
else:
    print('Digite um valor válido!')



