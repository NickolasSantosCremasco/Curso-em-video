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

