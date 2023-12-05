palavras = ('aprender','estudar','casa','mobilha','cama'
            'trabalhar','programar','futebol','dormir','falar',
            'gritar','amar','estranho','ajudar','amigo')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end= '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')