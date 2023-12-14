def moeda(n):
    return f'R${n:.2f}'


def metade(m, t=True):
    metade = m / 2
    if t:
        return f'R${metade:.2f}'
    else:
        return metade

def dobro(m, t=True):
    dobro = m * 2
    if t:
        return f'R${dobro:.2f}'
    else:
        return dobro




def aumentar(n, p, t=True):
    porcentagem = (n * p) / 100
    final = n + porcentagem
    if t:
        return f'R${final:.2f}'
    else:
        return final


def diminuir(n, p, t=True):
    porcentagem = (n * p) / 100
    final = n - porcentagem
    if t:
        return f'R${final:.2f}'
    else:
        return final


def resumo(p, au, re, t=True):
    '''
    -> Analise de preço, redução, metade, dobro e aumento
    :param p: valor a ser analisado
    :param au: aumento desejado que seja realizada a conta
    :param re: redução desejada que seja realizada a conta
    :return: Nenhum return feito
    '''

    print('-' * 30)
    print(f'{"RESUMO VALOR":^30}')
    print('-' * 30)
    if t:
        print(f'Preço analisado: {moeda(p):>13}')
        print(f'Dobro de preço: {dobro(p):>14}')
        print(f'Metade do preço: {metade(p):>13}')
        print(f'{au}% de aumento: {aumentar(p, au):>13}')
        print(f'{re}% de redução: {diminuir(p, re):>13}')
    else:
        print(f'\033[0;33mERRO! "{p}" Não é um número \033[m')





