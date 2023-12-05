expr = str(input('Digite a espressão: '))
pilha = []
 #Para cada simbro dentro da string, espressão digitada
for simb in expr:
    if simb == '(':
        # Se o elemento na str for ( ele vai adicionar a pilha
        pilha.append('(')

    elif simb == ')':
        #Se existir um elemento )
        if len(pilha) > 0:
            pilha.pop()
            #Ele verifica se o pilha é maior que 0, se sim ele retira o elemento que esta la dentro que era o (, fazendo um par perfeito
        else:
            pilha.append(')')
            break
            #Aqui é, se não for maior que 0 ele adiciona o ) a pilha fazendo a expr estar errada pois não formou um par
if len(pilha) == 0:
    #Se a pilha for maior que zero esta errado pois os parenteses não tiveram seus pares perfeitos
    print('Sua expressão está válida')
else:
    #Se a pilha for igual a zero deu tudo certo a expressão teve seus parenteses formando um par perfeito e não faltou nenhum na expressão
    print('Sua expressão esta errada! ')
